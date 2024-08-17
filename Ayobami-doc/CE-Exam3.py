#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 22:37:52 2024

@author: hosen-lab
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import exp1  # Importing the exponential integral function

# Constants
Q = 0.08  # Pumping rate (m^3/s)
T = 0.065  # Transmissivity (m^2/s)
rw = 0.3  # Radius of the well (m)
R = 200  # Radius of influence (m)

# Create an array of distances along the x-axis
x = np.linspace(0, R, 1000)

# Calculate drawdown for each distance
s = []
for distance in x:
    u = distance ** 2 / (4 * T * R ** 2)
    W_u = -exp1(u)
    s.append(Q / (4 * np.pi * T) * W_u)

# Plotting
plt.plot(x, s)
plt.xlabel('Distance from Well A (m)')
plt.ylabel('Drawdown (m)')
plt.title('Steady State Drawdown along the x-axis')
plt.grid(True)

# Save the plot as an image file (e.g., PNG)
plt.savefig('steady_state_drawdown.png')

# Show the plot
plt.show()
