# -*- coding: utf-8 -*-
"""
  run_doe.py generated by WhatsOpt. 
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 140

import numpy as np
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
from openmdao.api import Problem, SqliteRecorder, CaseReader
from whatsopt.smt_doe_driver import SmtDoeDriver
from branin import Branin 

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-b", "--batch",
                  action="store_true", dest="batch", default=False,
                  help="do not plot anything")
(options, args) = parser.parse_args()

pb = Problem(Branin())
pb.driver = SmtDoeDriver(sampling_method='LHS', n_cases=50)
case_recorder_filename = 'branin_doe.sqlite'        
recorder = SqliteRecorder(case_recorder_filename)
pb.driver.add_recorder(recorder)
pb.model.add_recorder(recorder)
pb.model.nonlinear_solver.add_recorder(recorder)


pb.model.add_design_var('x1', lower=-5, upper=10)
pb.model.add_design_var('x2', lower=0, upper=15)

pb.model.add_objective('f')


pb.model.add_constraint('g', upper=0.)

pb.setup()  
pb.run_driver()        

if options.batch:
    exit(0)
reader = CaseReader(case_recorder_filename)
cases = reader.system_cases.list_cases()
n = len(cases)
data = {'inputs': {}, 'outputs': {} }

data['inputs']['x1'] = np.zeros((n,)+(1,))
data['inputs']['x2'] = np.zeros((n,)+(1,))

data['outputs']['f'] = np.zeros((n,)+(1,))
data['outputs']['g'] = np.zeros((n,)+(1,))

for i, case_id in enumerate(cases):
    case = reader.system_cases.get_case(case_id)
    data['inputs']['x1'][i,:] = case.inputs['x1']
    data['inputs']['x2'][i,:] = case.inputs['x2']
    data['outputs']['f'][i,:] = case.outputs['f']
    data['outputs']['g'][i,:] = case.outputs['g']
      

output = data['outputs']['f'].reshape(-1)

input = data['inputs']['x1'].reshape(-1)
plt.subplot(2, 2, 1)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('f')
plt.xlabel('x1')

input = data['inputs']['x2'].reshape(-1)
plt.subplot(2, 2, 2)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('x2')


output = data['outputs']['g'].reshape(-1)

input = data['inputs']['x1'].reshape(-1)
plt.subplot(2, 2, 3)
plt.plot(input[0::1], output[0::1], '.')
plt.ylabel('g')
plt.xlabel('x1')

input = data['inputs']['x2'].reshape(-1)
plt.subplot(2, 2, 4)
plt.plot(input[0::1], output[0::1], '.')
plt.xlabel('x2')

plt.show()
