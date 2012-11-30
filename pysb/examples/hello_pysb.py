#!/usr/bin/env python
"""Hello PySB! (i.e. hello world) A simple model with a reversible binding rule.

(This is the example shown on the pysb.org home page.)
"""

from pysb import *
from pysb.integrate import odesolve
from pylab import linspace, plot, xlabel, ylabel, show

Model()

# Declare the monomers
Monomer('L', ['s'])
Monomer('R', ['s'])

# Declare the parameters
Parameter('L_0', 100)
Parameter('R_0', 200)
Parameter('kf', 1e-3)
Parameter('kr', 1e-3)

# Declare the initial conditions
Initial(L(s=None), L_0)
Initial(R(s=None), R_0)

# Declare the binding rule
Rule('L_binds_R', L(s=None) + R(s=None) <> L(s=1) % R(s=1), kf, kr)

# Observe the complex
Observable('LR', L(s=1) % R(s=1))

if __name__ == '__main__':
    # Simulate the model through 40 seconds
    time = linspace(0, 40, 100)
    print "Simulating..."
    x = odesolve(model, time)
    # Plot the trajectory of LR
    plot(time, x['LR'])
    xlabel('Time (seconds)')
    ylabel('Amount of LR')
    show()