"""
Simple Monte Carlo Pi Estimation
------------------------------

A basic implementation of the Monte Carlo method for estimating π (pi).
This script provides a quick and straightforward calculation without any
visualization or advanced features.

The estimation works by generating random points in a 2x2 square and
calculating the ratio of points that fall inside a unit circle to the
total number of points. This ratio, multiplied by 4, approximates π.

"""

import random

# Configuration
points_inside = 0
total_points = 1000000

# Generate random points and count those inside the unit circle
for _ in range(total_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x*x + y*y <= 1:
        points_inside += 1

# Calculate and display the estimation
pi_estimate = 4 * points_inside / total_points
print(f"Estimated value of π: {pi_estimate}")


