import numpy as np
from shapely.geometry import Polygon, MultiPolygon
import matplotlib.pyplot as plt

# Defining polygons in shapely

polygon = Polygon([[-2, 3], [-2, 6], [3, 6], [3, 3]])

plt.fill(*polygon.exterior.xy, color='red', edgecolor='black') # plot solid square
plt.scatter(polygon.exterior.xy[0], polygon.exterior.xy[1], edgecolor='black') # Plot corner points
plt.plot(polygon.boundary.xy[0], polygon.boundary.xy[1], color='orange') # plot boundary as a line
plt.scatter(polygon.centroid.x, polygon.centroid.y) # Plot single point at centroid
plt.xticks(np.arange(-3,5,1)) # adjust x axis limits
plt.yticks(np.arange(2, 8, 1)) # adjust y axis limits
# plt.show()

# Defining multipolygons in shapely

multipolygon = MultiPolygon([Polygon([[4, 4], [4, 6], [7, 6], [7, 4]]),
                             Polygon([[4, 0], [4, 3], [7, 3], [7, 0]])])

for geom in multipolygon.geoms:
    plt.fill(*geom.exterior.xy, color="purple", label="MultiPolygon")
    plt.scatter(geom.exterior.xy[0], geom.exterior.xy[1], color="purple",
                edgecolor="black")
plt.grid(ls="--", lw=1, alpha=0.6)
plt.xticks(np.arange(3, 9, 1))
plt.yticks(np.arange(-1, 8, 1))
plt.show()