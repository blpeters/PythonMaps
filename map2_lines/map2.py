import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import LineString

linestring = LineString([[2, 1], [1, 2], [1, 3], [0, 4]])
linestring.area

# Use the xy method from shapely to access a list of the coordinates

import matplotlib.pyplot as plt

# plt.plot(linestring.xy[0], linestring.xy[1], color='orange')
# plt.scatter(linestring.xy[0], linestring.xy[1], s=200, color='orange',
#             edgecolor='black')
# plt.grid(ls="--", lw=1, alpha=0.6)
# plt.xticks(np.arange(-1, 4, 1))
# plt.yticks(np.arange(0, 6, 1))
# plt.show()

# Use the shapely interpolate feature to add a point halfway along the length of the line
middle = linestring.length / 2
interpolated_linestring = linestring.interpolate(middle)

plt.plot(linestring.xy[0], linestring.xy[1], color='orange')
plt.scatter(linestring.xy[0], linestring.xy[1], s=200, color='orange',
             edgecolor='black')
plt.scatter(interpolated_linestring.xy[0], interpolated_linestring.xy[1], s=200,
            edgecolor='black')
plt.grid(ls="--", lw=1, alpha=0.6)
plt.xticks(np.arange(-1, 4, 1))
plt.yticks(np.arange(0, 6, 1))
plt.show()

# map 2: road network