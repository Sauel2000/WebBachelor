import matplotlib.pyplot as plt
import numpy as np

# Define the starting point and the reference vector
start = np.array([1, 2])
ref_vector = np.array([2, 1])

# Define the direction vector as perpendicular to the reference vector
direction = np.array([-ref_vector[1], ref_vector[0]])

# Define the two vectors by adding the direction vectors to the starting points
vector1 = start + direction
vector2 = start - direction
vector3 = 

# Create a 2D plot and plot the vectors
fig, ax = plt.subplots()
ax.quiver(start[0], -start[1], direction[0], -direction[1], color='r', angles='xy', scale_units='xy', scale=1, label="Direction vector")
ax.quiver(start[0], -start[1], vector1[0]-start[0], -vector1[1]+start[1], color='b', angles='xy', scale_units='xy', scale=1, label="Vector 1")
ax.quiver(start[0], -start[1], vector2[0]-start[0], -vector2[1]+start[1], color='g', angles='xy', scale_units='xy', scale=1, label="Vector 2")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_xlim([0, 6])
ax.set_ylim([-5, 0])
ax.legend()
plt.show()
