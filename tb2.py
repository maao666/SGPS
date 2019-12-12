import H159 as solver
from pprint import pprint

# Test bench 2
solver.set_similar('ar1', 'ar3')
#solver.set_perpendicular('sa1', 'sc1')
solver.set_parallel('sa2','sa4')

pprint(solver.get_all())
