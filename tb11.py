import H159 as solver
from pprint import pprint

# Test bench

solver.set_fraction('sb2', 'sc3', 2 / 3)
solver.set_fraction('sc2', 'sc3', 1.2)

pprint(solver.get_all())
