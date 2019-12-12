import H159 as solver
from pprint import pprint

# Test bench 8

solver.set_perpendicular('sb1', 'sc1')
solver.set_sum_value('sa2','sa4',4)
solver.set_equal('a1', 'b3')

pprint(solver.get_all())
