'''
This is a software tool that finds the convex hull of a set of points
given by their coordinates and displays it on the coordinate plane and 
saves the image in one of the graphic formats.
developed by Obrotskyi Myroslav group: KM-22.
'''
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import numpy as np

# Reading data fro the file DS7.txt
with open('DS7.txt', 'r') as file:
    data = np.loadtxt(file)

# Finding bulging skin
hull = ConvexHull(data)

# Canvas size
canvas_size = (960, 540)

# Creating graphic
fig, ax = plt.subplots(figsize=(canvas_size[0] / 100, canvas_size[1] / 100), dpi=100)
ax.set_xlim(0, canvas_size[0])
ax.set_ylim(0, canvas_size[1])

# Representation of the convex hull using segments of blue color
for simplex in hull.simplices:
    plt.plot(data[simplex, 0], data[simplex, 1], 'b-')

# Representation of the points of the original dataset together with the convex hull
plt.plot(data[:, 0], data[:, 1], 'ko')

# Saving the result in a graphic format file (PNG)
plt.savefig('convex_hull.png')

# Showing result
plt.show()
