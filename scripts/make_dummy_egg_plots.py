#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:18:07 2024

@author: dgaio
"""


import matplotlib.pyplot as plt
import numpy as np
import os 



def draw_radial_lines_plot(fig, ax, angles, lengths, circle_radius=10, color='orange'):
    """
    Draws radial lines and a central circle on the given Axes object.

    Parameters:
    - fig, ax: Figure and Axes objects from Matplotlib on which to draw.
    - angles: Array of angles for the radial lines.
    - lengths: Array of lengths for the radial lines.
    - circle_radius: Radius of the central circle. Defaults to 10.
    - color: Color of the radial lines. Defaults to 'orange'.
    """
    for length, angle in zip(lengths, angles):
        x_end = length * np.cos(angle)
        y_end = length * np.sin(angle)
        ax.plot([0, x_end], [0, y_end], color=color)

    center_circle = plt.Circle((0, 0), circle_radius, color='white', zorder=10)
    ax.add_artist(center_circle)
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.axis('off')
    ax.set_aspect('equal')



def save_plot(fig, output_folder, file_name):
    """
    Saves the plot as a PNG file and closes the figure.

    Parameters:
    - fig: Figure object from Matplotlib containing the plot to save.
    - output_folder: Folder where the plot will be saved.
    - file_name: Name of the file to save the plot as.
    """
    plt.savefig(f'{output_folder}/{file_name}.png', format='png', bbox_inches='tight')
    plt.close(fig)



def generate_biased_spokes(side, num_spokes=150):
    if side in ['top', 'bottom']:
        bias_factor = np.pi / 4
        angle_offset = np.pi / 2 if side == 'top' else -np.pi / 2
    else:
        bias_factor = 0
        angle_offset = 0
    angles = np.linspace(-np.pi + bias_factor + angle_offset, np.pi - bias_factor + angle_offset, num_spokes)
    lengths = np.random.rand(num_spokes) * 100
    return angles, lengths


# making egg plots
def create_multiple_radial_lines_plots(num_plots, output_folder):
    for i in range(num_plots):
        fig, ax = plt.subplots(figsize=(6, 6))
        num_spokes = np.random.randint(50, 150)
        lengths = np.random.rand(num_spokes) * 100
        angles = np.linspace(0, 2 * np.pi, num_spokes)
        draw_radial_lines_plot(fig, ax, angles, lengths)
        save_plot(fig, output_folder, f'radial_plot_{i+1}')

# making egg plots where top and bottom differ, but right and left not (on purpose)
def create_custom_radial_lines_plots(num_plots, output_folder):
    for i in range(num_plots):
        fig, ax = plt.subplots(figsize=(6, 6))
        accentuate_side = np.random.choice(['top', 'bottom', 'left', 'right'])
        angles, lengths = generate_biased_spokes(accentuate_side)  # Corrected line
        draw_radial_lines_plot(fig, ax, angles, lengths)
        save_plot(fig, output_folder, f'radial_plot_{i+1}_{accentuate_side}')

# making egg plots where both top and bottom as well as right and left differ
def create_advanced_radial_lines_plots(num_plots, output_folder):
    circle_radius = 10  # Size of the central circle

    for i in range(num_plots):
        fig, ax = plt.subplots(figsize=(6, 6))
        accentuate_sides = np.random.choice(['top', 'bottom', 'left', 'right'], 2, replace=False)
        num_spokes = np.random.randint(150, 200)  # Total number of spokes

        angles = []
        lengths = []

        for side in accentuate_sides:
            if side in ['top', 'bottom']:
                angle_range = np.pi / 3  # Narrower angle range for top/bottom
                angle_offset = 0 if side == 'top' else np.pi  # Offset angle for top/bottom
            else:
                angle_range = np.pi / 2  # Wider angle range for left/right
                angle_offset = -np.pi / 2 if side == 'left' else np.pi / 2  # Offset angle for left/right
            
            side_angles = np.linspace(angle_offset - angle_range, angle_offset + angle_range, num_spokes // 4)
            angles.extend(side_angles)
            side_lengths = np.random.rand(num_spokes // 4) * 120  # Longer spokes for accentuated sides
            lengths.extend(side_lengths)

        # Draw the radial lines
        for length, angle in zip(lengths, angles):
            x_end = length * np.cos(angle)
            y_end = length * np.sin(angle)
            ax.plot([0, x_end], [0, y_end], color='orange')

        # Draw the central circle
        center_circle = plt.Circle((0, 0), circle_radius, color='white', zorder=10)
        ax.add_artist(center_circle)
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)
        ax.axis('off')
        ax.set_aspect('equal')

        # Construct a label for the sides being accentuated
        side_label = '_'.join(accentuate_sides)
        plt.savefig(f'{output_folder}/radial_plot_{i+1}_{side_label}.png', format='png', bbox_inches='tight')
        plt.close(fig)




num_plots = 42
output_folder = '/Users/dgaio/Desktop/EGG_plots/'  


# egg plots 
create_multiple_radial_lines_plots(num_plots, output_folder)

# egg plots differing top from bottom: 
create_custom_radial_lines_plots(num_plots, output_folder)

# egg plots differing top from bottom and right from left: 
create_advanced_radial_lines_plots(num_plots, output_folder)






