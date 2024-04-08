#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 18:15:23 2024

@author: dgaio
"""

import cv2
import os
import glob

def convert_jpg_to_png_opencv(source_folder, output_folder=None):
    # Use the source folder for output if no output folder is provided
    if output_folder is None:
        output_folder = source_folder
    else:
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

    # Find all JPEG files in the source folder
    jpg_files = glob.glob(os.path.join(source_folder, '*.jpg'))

    for jpg_file in jpg_files:
        # Read the image using OpenCV
        img = cv2.imread(jpg_file)

        # Construct the output file path with a PNG extension
        base_name = os.path.basename(jpg_file)
        png_file = os.path.splitext(base_name)[0] + '.png'
        output_path = os.path.join(output_folder, png_file)

        # Save the image in PNG format
        cv2.imwrite(output_path, img)

    print(f"Converted {len(jpg_files)} images to PNG format in '{output_folder}'")

# Usage
source_folder = '/Users/dgaio/Downloads/flowers/rose'  # Replace with your JPEG images folder
output_folder = '/Users/dgaio/Downloads/flowers/rose/png'  # Replace with your desired output folder, or leave as None to use the source folder
convert_jpg_to_png_opencv(source_folder, output_folder)
