#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:47:13 2024

@author: dgaio
"""

import matplotlib.pyplot as plt
from skimage import io, color, feature, exposure
import numpy as np
from skimage import io, color, feature
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import os
import numpy as np
import os
import shutil


################################################################################


# PART 1: extract and inspect features 
    
folder_path = '/Users/dgaio/Desktop/EGG_plots'  

image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]

features = []

for file_name in image_files:
    image = io.imread(os.path.join(folder_path, file_name))
    if image.shape[-1] == 4:
        image = image[..., :3]  # Drop alpha channel if present
    image_gray = color.rgb2gray(image)
    
    # Extract HOG features
    hog_features = feature.hog(image_gray)
    features.append(hog_features)


# pick one feature array to summarize: 
feature_array = features[0]

# non-zero elements
non_zero_count = np.count_nonzero(feature_array)

mean = np.mean(feature_array)
std_dev = np.std(feature_array)

print(f"Summary of features for the first image:")
print(f"Total elements: {len(feature_array)}")
print(f"Non-zero elements: {non_zero_count}")
print(f"Mean: {mean:.4f}")
print(f"Standard Deviation: {std_dev:.4f}")

# =============================================================================
# # reduce dimensionality
# pca = PCA(n_components=5)  # Adjust n_components based on your needs
# features_reduced = pca.fit_transform(features)
# =============================================================================



################################################################################



# PART 2: clustering  


from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt

# Use linkage to compute the hierarchical clustering
Z = linkage(features, 'ward')  # 'ward' linkage minimizes the variance of clusters being merged

# Plot the dendrogram to visualize the clustering
plt.figure(figsize=(10, 7))
dendrogram(Z)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()


# Decide on a cutoff distance to define the clusters
cutoff_distance = 40  # This value depends on your dendrogram and desired number of clusters

# Use fcluster to form clusters from the hierarchical clustering defined by Z
clusters = fcluster(Z, cutoff_distance, criterion='distance')

# Now clusters contains the cluster assignment for each original data point (image feature vector in your case)



################################################################################


# PART 3: split into folders for inspection 


def organize_clusters_into_folders(folder_path, image_files, cluster_assignments):
    """
    Organizes images into folders based on their cluster assignments.

    Parameters:
    - folder_path: The path to the folder containing the original images.
    - image_files: A list of filenames for the images that were clustered.
    - cluster_assignments: A list/array of cluster IDs for each image.
    """
    base_path = os.path.dirname(folder_path)  # Get the base path of the folder
    clustered_folder_path = os.path.join(base_path, 'clustered')  # Path for the 'clustered' folder

    # Create the 'clustered' directory if it doesn't exist
    if not os.path.exists(clustered_folder_path):
        os.makedirs(clustered_folder_path)

    for file_name, cluster_id in zip(image_files, cluster_assignments):
        # Create a subfolder for the current cluster if it doesn't exist
        cluster_folder_path = os.path.join(clustered_folder_path, f'cluster_{cluster_id}')
        if not os.path.exists(cluster_folder_path):
            os.makedirs(cluster_folder_path)

        # Define the source and destination paths for the image
        src_path = os.path.join(folder_path, file_name)
        dst_path = os.path.join(cluster_folder_path, file_name)

        # Move the image to the appropriate cluster folder
        shutil.copy(src_path, dst_path)

    print(f"Images have been organized into cluster folders in '{clustered_folder_path}'.")

organize_clusters_into_folders(folder_path, image_files, clusters)


################################################################################

