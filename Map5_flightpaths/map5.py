import pandas as pd

airports = pd.read_csv("../map1_points/airports.csv",
                       delimiter=',',
                       names=['id', 'name', 'city', 'country', 'iata', 'icao', 'lat', 'long', 'altitude', 'timezone',
                              'dst', 'tz', 'type', 'source'])

routes = pd.read_csv("routes.csv",
                       delimiter=',',
                       names=['airline', 'id', 'source_airport', 'source_airport_id', 'destination_airport',
                              'destination_airport_id', 'codeshare', 'stops', 'equipment'])

# create a dataframe of linestrings joining the source airport to the destination airport for each route.
# step 1 - create a duplicate airports DataFrame and label one as source and one as destination
# step 2 - merge the source DataFrame with the routes using the routes source iata code
# step 3 - merge the destination DataFrame with the routes using the routes destiation iata code
# step 4 - use the lat and long values of the source and destinations to create a LineString for that route.

# step 1
source_airports = airports.copy()
destination_airports = airports.copy()
source_airports.columns = [str(col) + '_source' for col in source_airports.columns]
destination_airports.columns = [str(col) + '_destination' for col in destination_airports.columns]

#steps 2 and 3
routes = routes[['source_airport', 'destination_airport']]
routes = pd.merge(routes, source_airports, left_on='source_airport', right_on='iata_source')
routes = pd.merge(routes, destination_airports, left_on='destination_airport', right_on='iata_destination')

# step 4
import geopandas as gpd
from shapely.geometry import LineString

geometry = [LineString([[routes.iloc[i]['long_source'], routes.iloc[i]['lat_source']],
                        [routes.iloc[i]['long_destination'], routes.iloc[i]['lat_destination']]
                        ]) for i in range(routes.shape[0])
]

routes = gpd.GeoDataFrame(routes, geometry=geometry, crs='EPSG:4326')


import matplotlib.pyplot as plt
import cartopy.crs as ccrs
fig = plt.figure(facecolor='black')
ax = plt.axes(projection=ccrs.Robinson())
ax.patch.set_facecolor('black')

routes.plot(ax=ax, transform=ccrs.Geodetic(), color='white', linewidth=0.1, alpha=0.1)
ax.axis('off')

plt.setp(ax.spines.values(), color='black')
plt.setp([ax.get_xticklines(), ax.get_yticklines()], color='black')

plt.show()




