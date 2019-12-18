#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

require 'thrift'

module WhatsOpt
  module SurrogateServer
    module SurrogateKind
      SMT_KRIGING = 0
      SMT_KPLS = 1
      SMT_KPLSK = 2
      SMT_LS = 3
      SMT_QP = 4
      OPENTURNS_PCE = 5
      VALUE_MAP = {0 => "SMT_KRIGING", 1 => "SMT_KPLS", 2 => "SMT_KPLSK", 3 => "SMT_LS", 4 => "SMT_QP", 5 => "OPENTURNS_PCE"}
      VALID_VALUES = Set.new([SMT_KRIGING, SMT_KPLS, SMT_KPLSK, SMT_LS, SMT_QP, OPENTURNS_PCE]).freeze
    end

    class SurrogateException < ::Thrift::Exception
      include ::Thrift::Struct, ::Thrift::Struct_Union
      def initialize(message=nil)
        super()
        self.msg = message
      end

      def message; msg end

      MSG = 1

      FIELDS = {
        MSG => {:type => ::Thrift::Types::STRING, :name => 'msg'}
      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

    class SurrogateQualification
      include ::Thrift::Struct, ::Thrift::Struct_Union
      R2 = 1
      YP = 2

      FIELDS = {
        R2 => {:type => ::Thrift::Types::DOUBLE, :name => 'r2'},
        YP => {:type => ::Thrift::Types::LIST, :name => 'yp', :element => {:type => ::Thrift::Types::DOUBLE}}
      }

      def struct_fields; FIELDS; end

      def validate
      end

      ::Thrift::Struct.generate_accessors self
    end

  end
end
