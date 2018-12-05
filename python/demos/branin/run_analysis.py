# -*- coding: utf-8 -*-
"""
  run_analysis.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 140

from openmdao.api import Problem
from branin import Branin 

pb = Problem(Branin())
pb.setup()  

pb.run_model()   
pb.model.list_inputs(print_arrays=False)
pb.model.list_outputs(print_arrays=False)

