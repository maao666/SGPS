import H159 as solver
from pprint import pprint

# Test bench 3
solver.set_similar('ar1', 'ar3')
#solver.set_perpendicular('sa1', 'sc1')
solver.set_parallel('sa2','sa4')
solver.set_equal('a1', 'b1')

pprint(solver.get_all())
