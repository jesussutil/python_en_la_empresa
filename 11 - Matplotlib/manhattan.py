import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM
import matplotlib.pyplot as plt

osm_tiles = OSM()

plt.figure(figsize=(16, 16))

ax = plt.axes(projection=osm_tiles.crs)
ax.set_extent([-73.95,-74.01, 40.755, 40.785], ccrs.PlateCarree())
ax.add_image(osm_tiles, 14)

# Rutas
ax.plot([-73.959, -73.962, -73.9636, -73.973, -73.985,-73.9799572, -73.985,-73.9908905], [40.7828951, 40.7794366, 40.777, 40.7807909, 40.7635, 40.7614327, 40.7635, 40.7557994], color='black', linestyle='dotted', linewidth=3, transform=ccrs.PlateCarree())

# Puntos
ax.plot(-73.9799572, 40.7614327, color='red', linewidth=1, marker='o',transform=ccrs.Geodetic())
ax.text(-73.9799572, 40.7614327, 'MoMA',horizontalalignment='right',transform=ccrs.Geodetic())

ax.plot(-73.962, 40.7794366, color='red', linewidth=1, marker='o',transform=ccrs.Geodetic())
ax.text(-73.962, 40.7794366, 'Metropolitan Museum of Art',horizontalalignment='right',transform=ccrs.Geodetic())

ax.plot(-73.959, 40.7828951, color='red', linewidth=1, marker='o',transform=ccrs.Geodetic())
ax.text(-73.959, 40.7828951, 'Museo Guggenheim',horizontalalignment='right',transform=ccrs.Geodetic())

ax.plot(-73.9908905, 40.7557994, color='red', linewidth=1, marker='o',transform=ccrs.Geodetic())
ax.text(-73.9908905, 40.7557994, 'Madame Tussauds',horizontalalignment='right',transform=ccrs.Geodetic())

ax.plot(-73.973, 40.7807909, color='red', linewidth=1, marker='o',transform=ccrs.Geodetic())
ax.text(-73.973, 40.7807909, 'Museo de Historia Natural',horizontalalignment='right',transform=ccrs.Geodetic())

plt.show()
