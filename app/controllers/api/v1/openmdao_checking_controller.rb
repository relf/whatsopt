require 'whats_opt/openmdao_generator'

class Api::V1::OpenmdaoCheckingController < Api::ApiController 

  # POST /multi_disciplinary_analysis/{mda_id}/openmdao_checking
  def create
    params = openmdao_checking_params
      
    if params[:mda_id]
      mda = MultiDisciplinaryAnalysis.find(params[:mda_id])
      if mda
        ogen = WhatsOpt::OpenmdaoGenerator.new(mda)
        status, lines = ogen.check_mda_setup 
        render json: {status_ok: status, log: lines}
      else
        render json: {error: true} 
      end 
    else
      render json: {error: true} 
    end 
  end

  private

  def openmdao_checking_params
    params.require(:openmdao_checking).permit(:mda_id)
  end
  
end
