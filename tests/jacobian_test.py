from bioscrape.types import Model
from bioscrape.simulator import py_simulate_model, ModelCSimInterface
import numpy as np

M_path = 'C:\\Users\\wp_ix\\OneDrive\\Caltech\\Code\\bioscrape\\examples\\models\\'
M_names = ["gene_expression_with_delay.xml"]#, "sbml_test.xml", "repressilator_sbml.xml"]

for m_name in M_names:
	f = open(M_path+m_name)
	f.close()

	print("Trying Model:", m_name)
	M_loaded = Model(filename = M_path+m_name)

	s = ModelCSimInterface(M_loaded)

	state = M_loaded.get_species_array()
	jacobian = np.zeros((state.size, state.size))
	s.py_prep_deterministic_simulation()
	s.py_prep_deterministic_jacobian()
	s.py_compute_jacobian(state, jacobian, 0)

	#Change the induction time
	#NOTE That changing a model loaded from xml will not change the underlying XML.
	#M_loaded.set_parameter("T", 50)

	#Simulate the Model deterministically
	#timepoints = np.arange(0, 150, 1.0)
	#results_det = py_simulate_model(timepoints, Model = M_loaded, stochastic = False, use_jacobian = True) #Returns a Pandas DataFrame
	#print("Simulation Finished")