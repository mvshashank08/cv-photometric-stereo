import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

X = np.load("points.npy")
colors = np.load("colors.npy")
print("X: {0}, colors: {1}".format(X.shape, colors.shape))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[0, :], X[1, :], X[2, :], c=colors)
ax.set_xlim3d([-750, 750])
ax.set_ylim3d([-750, 750])
ax.set_zlim3d([-750, 750])
plt.show()