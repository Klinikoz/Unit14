"""
Program Name: heartplot.py
Author: Fahim Khan
Purpose: This program plots a heart curve using parametric equations and the matplotlib library.
Date: August 6, 2025
"""

import math
import matplotlib.pyplot as plt

# Create lists for x and y values
x_values = []
y_values = []

# Generate values using parametric equations for a heart curve
# t from 0 to 2*pi with fine increments
for i in range(0, 360):
    t = math.radians(i)
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    x_values.append(x)
    y_values.append(y)

# Plotting the graph
plt.figure()
plt.plot(x_values, y_values, color='red')
plt.title("Heart Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')  # Equal aspect ratio for x and y axes
plt.grid(True)
plt.show()
