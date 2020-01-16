# import numpy as np
from devito import Grid, Eq, solve, TimeFunction, Operator, configuration
from examples.cfd import plot_field, init_hat

configuration['openmp'] = 1
configuration['dse'] = 'advanced'
configuration['dle'] = 'advanced'

# Some variable declarations
nx = 81
ny = 81
nt = 100
c = 1.
dx = 2. / (nx - 1)
dy = 2. / (ny - 1)
print("dx %s, dy %s" % (dx, dy))
sigma = .2
dt = sigma * dx

grid = Grid(shape=(nx, ny), extent=(2., 2.))
u = TimeFunction(name='u', grid=grid, time_order=2, space_order=8)
init_hat(field=u.data[0], dx=dx, dy=dy, value=2.)

pde = u.laplace

op = Operator(Eq(u.forward, pde))

print(op.ccode)

op(time=2000)
