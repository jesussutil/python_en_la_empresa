import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM
import matplotlib.pyplot as plt

osm_tiles = OSM()

# usamos la proyección de OSM.
ax = plt.axes(projection=osm_tiles.crs) 

# Enventanamos en Manhattan
ax.set_extent([-73.8,-74.1, 40.66, 40.86]) 

# añadimos las losetas de OSM de nivel 12 de zoom (de 1 a 19).
ax.add_image(osm_tiles, 12) 

plt.show()
