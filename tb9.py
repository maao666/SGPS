import H159 as solver
from pprint import pprint

# Test bench 9 

solver.set_perpendicular('sa3', 'sc4')
#solver.set_sum_value('sa2','sa4',4)
solver.set_equal('c2', 'a3')

pprint(solver.get_all())
