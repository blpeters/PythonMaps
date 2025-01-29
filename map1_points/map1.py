import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

ports = pd.read_csv("wpi.csv")
portgeometry = [Point(xy) for xy in zip(ports['Longitude'], ports['Latitude'])]
port_geodata = gpd.GeoDataFrame(ports, crs="EPSG:4326", geometry=portgeometry)

# OPTION 1 - TRANSFORM THE CRS TO MERCATOR IN THE GEODATAFRAME

# reproject to world mercator
port_geodata = port_geodata.to_crs("EPSG:3395")

import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# port_geodata.plot(ax=ax, markersize=1, alpha=1, marker="+", color="green", linewidth=0.1)
# plt.show()

# OPTION 2 - KEEP THE EXISTING CRS UNTOUCHED IN THE GEODATAFRAME, BUT REPROJECT WITH CARTOPY
# This may be desireable if wanting to work further on the original geodataframe

# Use Cartopy to perform Robinson projection on the axis plotting object in matplotlib:

import cartopy.crs as ccrs

port_geodata = port_geodata.to_crs("EPSG:4326")

# Add in the Airport locations from a separate file to be added to the same plot. Similar to ports above

airports = pd.read_csv("airports.csv", delimiter=',',
                       names=['id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'long', 'altitude', 'timezone',
                              'dst', 'tz', 'type', 'source'])

airport_geometry = [Point(xy) for xy in zip(airports['long'], airports['lat'])]

airport_geodata = gpd.GeoDataFrame(airports,
                                   crs="EPSG:4326",
                                   geometry=airport_geometry)
# Make the matplotlib plot
fig, ax = plt.subplots(facecolor='black',
                       subplot_kw={'projection': ccrs.Robinson()})
ax.patch.set_facecolor('black') # Sets border to the same color as the background to make it invisible.

airport_geodata.plot(ax=ax, transform=ccrs.PlateCarree(),
                  markersize=4, alpha=1, edgecolors='none', color='crimson')
port_geodata.plot(ax=ax, transform=ccrs.PlateCarree(),
                  markersize=3, alpha=1, edgecolors='none', color='lightblue') # PlateCarree projection is used by
# Cartopy as a starting projection to understand how to transform to Robinson. Needs a starting point.

plt.setp(ax.spines.values(), color='black')
plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')
plt.show()

