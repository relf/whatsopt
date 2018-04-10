# -*- coding: utf-8 -*-
"""
  disc2_base.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 109

import numpy as np
from openmdao.api import ExplicitComponent

class Disc2Base(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate Disc2 discipline """

    def setup(self):
		
        self.add_input('y1', val=1.0, desc='')
        self.add_input('z', val=np.ones((2,)), desc='')
		
        self.add_output('y2', val=1.0, desc='')
#        self.declare_partials('*', '*')
		
#    def compute(self, inputs, outputs):
#        """ Disc2 computation """
    
#        outputs['y2'] = 1.0   
				
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Disc2 """
    
   		
#       	partials['y2', 'y1'] = np.zeros((1, 1))
#       	partials['y2', 'z'] = np.zeros((1, 2))        

        