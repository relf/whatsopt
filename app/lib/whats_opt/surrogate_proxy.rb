# frozen_string_literal: true

require "thrift"
require "securerandom"
require "surrogate_store"

module WhatsOpt
  class SurrogateProxy
    attr_reader :surrogate_id, :pid, :host, :port

    PYTHON = APP_CONFIG["python_cmd"] || "python"
    OUTDIR = File.join(Rails.root, "upload", "surrogate_store")

    DEFAULT_HOST = "localhost"
    DEFAULT_PORT = 41400

    def initialize(surrogate_id: nil, host: DEFAULT_HOST, port: DEFAULT_PORT, server_start: true)
      @host = host
      @port = port
      socket = Thrift::Socket.new(@host, @port)
      @transport = Thrift::BufferedTransport.new(socket)
      protocol = Thrift::BinaryProtocol.new(@transport)
      @client = Services::SurrogateStore::Client.new(protocol)

      @surrogate_id = surrogate_id || SecureRandom.uuid

      if server_start && !server_available?
        cmd = "#{PYTHON} #{File.join(Rails.root, 'services', 'run_server.py')} --outdir #{OUTDIR}"
        Rails.logger.info cmd
        @pid = spawn(cmd, [:out, :err] => File.join(Rails.root, "log", "whatsopt_server.log"))
        retries = 0
        while retries < 10 && !server_available?  # wait for server start
          retries += 1
          sleep(1)
        end
      end
    end

    def server_available?
      _send { @client.ping }
    end

    def self.shutdown_server(host: DEFAULT_HOST, port: DEFAULT_PORT)
      socket = Thrift::Socket.new(host, port)
      transport = Thrift::BufferedTransport.new(socket)
      protocol = Thrift::BinaryProtocol.new(transport)
      client = Services::SurrogateStore::Client.new(protocol)
      transport.open()
      client.shutdown
    rescue => e
      Rails.logger.warn e
    else
      transport.close()
    end

    def self.kill_server(pid)
      if pid
        Process.kill("TERM", pid)
        Process.waitpid pid
      end
    end

    def create_surrogate(surrogate_kind, x, y, options={}, uncertainties=[])
      opts = {}
      options.each do |ks, v|
        k = ks.to_s
        opts[k] = Services::OptionValue.new(vector: JSON.parse(v)) if v =~ /^\[.*\]$/
        opts[k] = Services::OptionValue.new(integer: v.to_i) if v == v.to_i.to_s
        opts[k] = Services::OptionValue.new(number: v.to_f) if (!opts[k] && v =~ /^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$/)
        opts[k] = Services::OptionValue.new(str: v.to_s) unless opts[k]
      end 
      uncs = uncertainties.map {|us| 
        u = us.map {|k, v| [k.to_sym, v]}.to_h
        Services::Distribution.new(name: u[:name], kwargs: u[:kwargs].map{|ks, v| [ks.to_s, v.to_f]}.to_h ) unless u.blank?
      }.compact
      _send { @client.create_surrogate(@surrogate_id, surrogate_kind, x, y, opts, uncs) }
    end

    def qualify(xv, yv)
      quality = nil
      _send { quality = @client.qualify(@surrogate_id, xv, yv) }
      quality
    end

    def predict_values(x)
      values = []
      _send {
        values = @client.predict_values(@surrogate_id, x)
      }
      values
    end

    def destroy_surrogate
      _send { @client.destroy_surrogate(@surrogate_id) }
    end

    def copy_surrogate(src_id)
      _send { @client.copy_surrogate(src_id, @surrogate_id) }
    end

    def get_sobol_pce_sensitivity_analysis
      sobol_indices = nil
      _send { sobol_indices = @client.get_sobol_pce_sensitivity_analysis(@surrogate_id) }
      sobol_indices
    end

    def _send
      @transport.open()
      yield
    rescue Services::SurrogateException => e
      # puts "#{e}: #{e.msg}"
      Rails.logger.warn "#{e}: #{e.msg}"
      raise
    rescue Thrift::TransportException => e
      # puts "#{e}"
      Rails.logger.warn e
      false
    else
      true
    ensure
      @transport.close()
    end
  end
end
