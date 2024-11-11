# Course: Numerical Analysis / MAD3703
# Project: Comparing Monte Carlo Approximation and Numerical Integration Approximation of π.
# Name: Tyler Boshaw
# Draft Due Date: Nov 22, 2024
# Final Due Date: Dec 6, 2024

# --------------------------------------------------------------------------- #
# Imports
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import math
import time

# --------------------------------------------------------------------------- #
## Technique - 1 / Monte Carlo Approximation
def monte_carlo():
    # start time (for measuring speed of approximation)
    start_time = time.time()

    # define the number of points for the test
    num_points = 1000
    
    # create some data to track trade-offs later
    point_range = []
    error_range = []
    time_range = []
    approx_range = []

    for i in range(num_points):
        # define x any y, creating a circular coordinate system for random points
        x = np.random.uniform(-1, 1, num_points)
        y = np.random.uniform(-1, 1, num_points)

        # distinguish the points inside the circular region
        bound = ((x**2 + y**2) <= 1)
        inside = np.sum(bound)

        # approximate π for the cirle
        approx = 4 * (inside / num_points)

        # calculate error to math.pi
        error = abs(math.pi - approx)

        # calculate the time taken for approximation
        end_time = time.time()
        duration = end_time - start_time

        # append info for trade-offs
        point_range.append(i)
        error_range.append(error)
        time_range.append(duration)
        approx_range.append(approx)

    # results with speed
    print(f"Monte Carlo Approximation of π with {num_points} points: {approx}")
    print(f"Speed of Approximation: {duration} seconds")
    print(f"Error of Approximation: {error}")

# === === === === === === === === === === === === === === === === === #

    ## Visualization of Approximation
    # create a plot for the data points to visual the approximation
    plt.figure(figsize=(8,8))
    plt.scatter(x[bound], y[bound], color="blue", s=2)
    plt.scatter(x[~bound], y[~bound], color="red", s=2)
    
    # plot the circular boundary
    circle = plt.Circle((0, 0), 1, color="black", fill=False, linewidth=2)
    plt.gca().add_artist(circle)
    
    # set plot limits and labels
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo Approximation of π with {num_points} points: {approx}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
# === === === === === === === === === === === === === === === === === #

    ## Visualization of Error and Speed Trade-off
    plt.figure(figsize=(12, 6))

    # plotting the error vs number of points
    plt.subplot(1, 3, 1)
    plt.plot(point_range, error_range, marker='', color='blue', linestyle='-', label='Error')
    plt.title("Error vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Error")
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    plt.legend()

    # plotting the time vs number of points
    plt.subplot(1, 3, 2)
    plt.plot(point_range, time_range, marker='', color='blue', linestyle='-', label='Time')
    plt.title("Time vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.legend()

    # plotting the approximation vs number of points
    plt.subplot(1, 3, 3)
    plt.plot(point_range, approx_range, marker='', color='blue', linestyle='-', label='Approximation')
    plt.title("Approximation vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Approximation")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

    return 
monte_carlo()

# --------------------------------------------------------------------------- #
## Technique - 2 / Numerical Integration Approximation
def num_int():
    print("TEST")




## Visualization of Approximation




## Visualization of Error and Speed Trade-off

# --------------------------------------------------------------------------- #