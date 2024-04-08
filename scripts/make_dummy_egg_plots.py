#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:18:07 2024

@author: dgaio
"""


import matplotlib.pyplot as plt
import numpy as np

# Function to create multiple plots with radial lines (spokes) where each plot is different
def create_multiple_radial_lines_plots(num_plots):
    # Define the size of the white circle
    circle_radius = 10

    for i in range(num_plots):
        fig, ax = plt.subplots(figsize=(6, 6))

        # Define the number of spokes
        num_spokes = np.random.randint(50, 150)

        # Create random lengths and angles for the spokes
        lengths = np.random.rand(num_spokes) * 100
        angles = np.linspace(0, 2 * np.pi, num_spokes)

        for length, angle in zip(lengths, angles):
            # Define the end point of the spoke
            x_end = length * np.cos(angle)
            y_end = length * np.sin(angle)
            # Plot the line from the center to the end point
            ax.plot([0, x_end], [0, y_end], color='skyblue')

        # Draw a white circle at the center to mimic the white space in the uploaded image
        center_circle = plt.Circle((0, 0), circle_radius, color='white', zorder=10)
        ax.add_artist(center_circle)

        # Set limits
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)
        
        # Hide the axes
        ax.axis('off')

        # Set aspect of the plot to be equal
        ax.set_aspect('equal')
        
        # Instead of displaying the plot, save it as a PNG file with a sequential number
        plt.savefig(f'/Users/dgaio/Desktop/EGG_plots/radial_plot_{i+1}.png', format='png')

        
        # Display the plot
        #plt.show()
        
        # Clear the current figure after saving to avoid memory issues
        #plt.clf()

# Call the function to create and save multiple plots
create_multiple_radial_lines_plots(42)


# try assigning phyla colors (now simulated). see if clustering is better 





