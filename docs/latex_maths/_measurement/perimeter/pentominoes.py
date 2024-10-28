import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

# Define the dictionary with pentomino shapes as tiles
pentominoes_tiles_dict = {
    'T': [
        (1, 0), (0, 1), (1, 1), (2, 1), (1, 2)
    ],
    'U': [
        (0, 0), (0, 1), (1, 1), (2, 1), (2, 0)
    ],
    'V': [
        (0, 0), (0, 1), (0, 2), (1, 2), (2, 2)
    ],
    'W': [
        (0, 0), (1, 0), (1, 1), (2, 1), (2, 2)
    ],
    'X': [
        (1, 0), (0, 1), (1, 1), (2, 1), (1, 2)
    ],
    'Y': [
        (0, 0), (0, 1), (0, 2), (0, 3), (1, 2)
    ],
    'Z': [
        (0, 0), (1, 0), (1, 1), (2, 1), (2, 2)
    ],
    'F': [
        (0, 0), (1, 0), (1, 1), (2, 1), (1, 2)
    ],
    'I': [
        (0, 0), (0, 1), (0, 2), (0, 3), (0, 4)
    ],
    'L': [
        (3, 1), (3, 0), (0, 0), (0, 4), (1, 4), (1, 1)
    ],
    'P': [
        (0, 0), (1, 0), (0, 1), (1, 1), (0, 2)
    ],
    'N': [
        (0, 0), (1, 0), (2, 0), (2, 1), (3, 1)
    ],
}

# Function to plot a shape and calculate its convex hull
def plot_shape_and_hull(coords):
    coords = np.array(coords)
    if len(np.unique(coords[:, 0])) == 1 or len(np.unique(coords[:, 1])) == 1:
        # Add a small variation to avoid the Qhull error
        coords = coords + np.random.normal(0, 0.01, coords.shape)
    hull = ConvexHull(coords)

    plt.fill(*coords.T)
    for simplex in hull.simplices:
        plt.plot(coords[simplex, 0], coords[simplex, 1], 'k-')

    return coords[hull.vertices].tolist()

# Plot each shape and calculate the convex hull vertices
plt.figure(figsize=(12,12))
pentominoes_hull_dict = {}
for i,key in enumerate(pentominoes_tiles_dict):
    plt.subplot(4,4,i+1)
    hull_vertices = plot_shape_and_hull(pentominoes_tiles_dict[key])
    pentominoes_hull_dict[key] = hull_vertices
    plt.title(key)
plt.tight_layout()
plt.show()

pentominoes_hull_dict
