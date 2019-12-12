import H159 as solver
from pprint import pprint

# Test bench 7
#solver.set_congruent('ar1', 'ar3')
#solver.set_perpendicular('sa1', 'sc1')
solver.set_equal('c6','c3')
#solver.set_equal('a1', 'b1')

pprint(solver.get_all())
