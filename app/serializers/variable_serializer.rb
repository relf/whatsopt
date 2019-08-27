# frozen_string_literal: true

class VariableSerializer < ActiveModel::Serializer
  attributes :name, :io_mode, :shape, :type, :desc, :units, :active

  has_one :parameter, key: :parameter_attributes
  has_one :scaling

  # class ParameterSerializer < ActiveModel::Serializer
  #   attributes :init, :lower, :upper
  # end

  # class ScalingSerializer < ActiveModel::Serializer
  #   attributes :ref, :ref0, :res_ref
  # end
end
