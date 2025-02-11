import osgeo
import dask.array as da
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from rasterio.plot import show
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap

with rasterio.open('marsDEM.tif') as src:
    mars_file = da.from_array(src.read(), chunks=(1, 1024, 1024))

print(f"Raster shape: {mars_file.shape}")
print(f"Chunks: {mars_file.chunksize}")

# compute the data from dask
computed_mars = mars_file.compute()

fig, ax = plt.subplots()
fig.set_size_inches(14,7)

show(computed_mars[0], cmap='viridis')
ax.axis('off')

plt.show()
