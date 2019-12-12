import H159 as solver
from pprint import pprint

# Test bench 10
solver.set_congruent('ar1', 'ar3')
#solver.set_perpendicular('sa1', 'sc1')
solver.set_similar('ar2','ar6')

pprint(solver.get_all())
