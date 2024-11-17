# Course: Numerical Analysis / MAD3703
# Project: Comparing Monte Carlo Approximation and Trapezoidal Rule Approximation of π.
# Name: Tyler Boshaw
# Draft Due Date: Nov 22, 2024
# Final Due Date: Dec 6, 2024

# --------------------------------------------------------------------------- #
# Imports
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import math
import time

# --------------------------------------------------------------------------- #
## Technique - 1 / Monte Carlo Approximation
def monte_carlo():
    # start time (for measuring speed of approximation)
    start_time = time.time()

    # define the number of points for the test
    num_points = 100000
    
    # create some data to track trade-offs later
    point_range = []
    error_range = []
    time_range = []
    approx_range = []

    for i in range(0, num_points, 100):
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
    btr = LinearSegmentedColormap.from_list("BlackRed", ["black", "red"])
    colorway = btr(np.linspace(0, 1, len(point_range)))
    plt.figure(figsize=(12, 6))
    

    # plotting the error vs number of points
    plt.subplot(1, 3, 1)
    #plt.plot(point_range, error_range, marker='', color='blue', linestyle='-', label='Error')
    plt.scatter(point_range, error_range, color=colorway,s=3)
    plt.title("Error vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Error")
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    #plt.legend()

    # plotting the time vs number of points
    plt.subplot(1, 3, 2)
    #plt.plot(point_range, time_range, marker='', color='blue', linestyle='-', label='Time')
    plt.scatter(point_range, time_range, color='black',s=3)
    plt.title("Time vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    #plt.legend()

    # plotting the approximation vs number of points
    plt.subplot(1, 3, 3)
    #plt.plot(point_range, approx_range, marker='', color='blue', linestyle='-', label='Approximation')
    plt.scatter(point_range, approx_range, color=colorway,s=3)
    plt.title("Approximation vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Approximation")
    plt.grid(True)
    #plt.legend()

    plt.tight_layout()
    plt.show()

    return 

# --------------------------------------------------------------------------- #
## Technique - 2 / Trapezoid Rule Approximation
def function(x):
    # define a function to integrate
    func = np.sqrt(np.clip(1 - x**2, 0, None))

    return func

def trap_rule():
    # start time (for measuring speed of approximation)
    start_time = time.time()

    # create some data to track trade-offs later
    point_range = []
    error_range = []
    time_range = []
    approx_range = []

    # define number of intervals (should ultimately determine accuracy)
    num_points = 1000

    for i in range(0, num_points, 10):

        # define bounds for integration
        b = math.pi
        a = 0

        ## trapezoidal rule algorithm

        # interval generation
        x = np.linspace(a, b, num_points)
        # evaluating the function at each subinterval point
        y = function(x)
        # step size calculation
        h = (b - a) / (num_points - 1) 
        # approximate the function using the trapezoidal rule
        trap = (h / 2) * (y[0] + 2 * np.sum(y[1:-1] + y[-1]))

        # approximate PI
        approx = 4 * trap

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
    
    print(f"Trapezoidal Rule Approximation of π with {num_points} points: {approx}")
    print(f"Speed of Approximation: {duration} seconds")
    print(f"Error of Approximation: {error}")
    
    # === === === === === === === === === === === === === === === === === #

    ## Visualization of Error and Speed Trade-off
    btr = LinearSegmentedColormap.from_list("BlackRed", ["black", "red"])
    colorway = btr(np.linspace(0, 1, len(point_range)))
    plt.figure(figsize=(12, 6))
    
    # plotting the error vs number of points
    plt.subplot(1, 3, 1)
    #plt.plot(point_range, error_range, marker='', color='blue', linestyle='-', label='Error')
    plt.scatter(point_range, error_range, color=colorway,s=3)
    plt.title("Error vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Error")
    plt.yscale('log')
    plt.xscale('log')
    plt.grid(True)
    #plt.legend()

    # plotting the time vs number of points
    plt.subplot(1, 3, 2)
    #plt.plot(point_range, time_range, marker='', color='blue', linestyle='-', label='Time')
    plt.scatter(point_range, time_range, color='black',s=3)
    plt.title("Time vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    #plt.legend()

    # plotting the approximation vs number of points
    plt.subplot(1, 3, 3)
    #plt.plot(point_range, approx_range, marker='', color='blue', linestyle='-', label='Approximation')
    plt.scatter(point_range, approx_range, color=colorway,s=3)
    plt.title("Approximation vs Number of Points")
    plt.xlabel("Number of Points")
    plt.ylabel("Approximation")
    plt.grid(True)
    #plt.legend()

    plt.tight_layout()
    plt.show()

    return 

# --------------------------------------------------------------------------- #
## Main Menu
def main():
    # menu for choosing method to run
    print(" -- Please choose an algorithm to approximate PI -- ")
    print(" >> a) Monte Carlo Method")
    print(" >> b) Trapezoidal Rule Integration")
    choice = input(">> ")

    if (choice == "a" or choice == "A"):
        print("// Processing //")
        monte_carlo()
    elif (choice == "b" or choice == "B"):
        print("// Processing //")
        trap_rule()
    else:
        print("###/ ERROR: Please select a valid option /###")
        main()

main()
# --------------------------------------------------------------------------- #