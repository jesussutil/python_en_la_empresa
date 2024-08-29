import cartopy.io.img_tiles as cimgt
import matplotlib.pyplot as plt
import geopandas as gpd
import fiona
fiona.drvsupport.supported_drivers['KML'] = 'rw'

polys = gpd.read_file('colada.kml', driver='KML')
polys = polys.to_crs("EPSG:3857")

fig = plt.plot()

gm_tiles = cimgt.GoogleTiles()

ax1 = plt.axes(projection=gm_tiles.crs)
ax1.set_extent([-17.964,-17.845, 28.644, 28.587])
ax1.add_image(gm_tiles, 14)

polys.plot(ax=ax1, alpha = 0.5, color="red")

plt.show()
