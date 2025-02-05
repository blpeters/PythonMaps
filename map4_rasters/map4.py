import osgeo
import rasterio

cattle = rasterio.open('GLW4-2020.D-DA.CTL.tif')
print(cattle.crs)

# Rasterio show command is basically a matplotlib imshow in a wrapper for geospatial data
# show takes a dataset object and renders it into a plot. single-band (gray) or multi-band (color)
# compatible with matplotlib for customization!

from rasterio.plot import show
# show(cattle)

# Load world country boundaries
import geopandas as gpd

df = gpd.read_file("..\\map2_lines\\natural_earth\\ne_10m_admin_0_countries.shp")
df = df[df['CONTINENT'] != 'Antarctica']
df['boundary'] = df.geometry.boundary
df['geometry'] = df['boundary'].copy()

# Always create a custom colormap when plotting a heatmap to account for the distribution of the data.
# reds is a base color map from matplotlib

import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap
from matplotlib import colors

bounds = [5, 10, 20, 50, 100, 250, 1000, 2500, 5000, 100000]

reds = cm.get_cmap("Reds", len(bounds))
newcolors = reds(np.linspace(0, 1, len(bounds)))
cmap = ListedColormap(newcolors)
norm = colors.BoundaryNorm(bounds, cmap.N)

# Add vector data to the raster plot and project everything on the Robinson projection

import matplotlib.pyplot as plt
from cartopy import crs as ccrs

fig = plt.figure(facecolor='white')
fig.set_size_inches(7, 3.5)
ax = plt.axes(projection=ccrs.Robinson())

show(cattle, ax=ax, cmap=cmap, norm=norm)
df.plot(ax=ax, edgecolor='black', lw=0.06, alpha=1, transform=ccrs.Geodetic())

cax = fig.add_axes([0.5, 0.2, 0.15, 0.015])
cb_ticks = [bounds[i] + (bounds[i+1] - bounds[i]) / 2 for i in range(len(bounds) - 1)]
cb = fig.colorbar(plt.cm.ScalarMappable(cmap=cmap, norm=norm), cax=cax,
orientation="horizontal", pad=0, format='%.3g', ticks=cb_ticks, drawedges=False)
cb.ax.set_xticklabels([str(val) for val in bounds[1:]])
cb.outline.set_visible(False)
cb.ax.tick_params(labelsize=4, width=0.2, length=0.75, rotation=60, color='black')
plt.setp(plt.getp(cb.ax, 'xticklabels'), color='black')
cb.ax.set_xlabel(f'Cattle Density', fontsize=5, color='black', labelpad=0)

ax.axis('off')
plt.show()

