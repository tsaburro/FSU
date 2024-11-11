# Course: Numerical Analysis
# Project: Comparing Monte Carlo Approximation and __ Approximation of PI.
# Name: Tyler Boshaw
# Draft Due Date: Nov 22, 2024


# Imports
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

## [[ Technique #1 ]]
# Monte Carlo Approximation
def mc_estimate_pi(num_points):
    inside_points = []
    outside_points = []
    
    # Initialize current number of points inside the circle
    inside_circle = 0

    for i in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
    
        # Check if the point is inside the quarter circle
        if x**2 + y**2 <= 1:
            inside_circle += 1
            inside_points.append((x,y))
        else:
            outside_points.append((x,y))

    # Calculate the approximation of pi
    pi_estimate = 4 * (inside_circle / num_points)
    
    # Plotting
    plt.figure(figsize=(8, 8))
    plt.scatter(inside_points, color="blue", s=1)
    plt.scatter(outside_points, color="red", s=1)
    plt.xlabel("Inside Points [N0] = \nOutside Points [N1] = ")
    plt.title(f"Monte Carlo Approximation of π (Estimate = {pi_estimate:.6f})")
    plt.legend()
    plt.show()
    
    return pi_estimate

# Set the number of points to sample
num_points = 10000
pi_approx = mc_estimate_pi(num_points)
print(f"Approximation of π with {num_points} points: {pi_approx}")



# Other Approximation Technique
def other_estimate_pi():
    print("test")



other_estimate_pi()


