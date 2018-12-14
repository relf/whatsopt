# -*- coding: utf-8 -*-
"""
  mod_branin_base.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 49

import numpy as np
from openmdao.api import Problem, Group
from openmdao.api import IndepVarComp
from openmdao.api import NonlinearBlockGS, ScipyKrylov

from mod_branin_function import ModBraninFunction

class ModBraninBase(Group):
    """ An OpenMDAO base component to encapsulate ModBranin MDA """
    
    def setup(self): 
    
    
        indeps = self.add_subsystem('indeps', IndepVarComp(), promotes=['*'])
		
        indeps.add_output('x1', 1.0)
        indeps.add_output('x2', 1.0)		    
 		
 		
        self.add_subsystem('ModBraninFunction', self.create_mod_branin_function(), promotes=['x1', 'x2', 'f', 'g'])         

        self.nonlinear_solver = NonlinearBlockGS() 
        self.linear_solver = ScipyKrylov()

    
    def create_mod_branin_function(self):
    	return ModBraninFunction()
    