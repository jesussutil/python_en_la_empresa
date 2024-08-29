import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cartopy.io.img_tiles import OSM

# usamos una proyección equirrectangular
ax = plt.axes(projection=ccrs.PlateCarree()) 

# Muestra el contorno de la costa.
ax.coastlines() 

# Imagen de archivo de la tierra de baja resolución.
ax.stock_img() 

plt.plot(-75, 43, color='red', linewidth=1, marker='o',transform=ccrs.Geodetic())
plt.text(-73.5, 44, 'New York',horizontalalignment='right',transform=ccrs.Geodetic())

# pintamos las losetas de Open Street Maps
osm_tiles = OSM() 
ax.add_image(osm_tiles, 1)

plt.show()
