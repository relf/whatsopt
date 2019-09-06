# frozen_string_literal: true

class AttachmentsController < ApplicationController
  # GET /attachements/1
  def show
    @attachment = Attachment.find(params[:id])
    authorize @attachment
    case params[:format]
    when "x3d"
      send_file @attachment.data.path(:x3d),
                type: @attachment.data_content_type,
                disposition: "inline"
    else
      send_file @attachment.data.path,
                type: @attachment.data_content_type
    end
  end
end
