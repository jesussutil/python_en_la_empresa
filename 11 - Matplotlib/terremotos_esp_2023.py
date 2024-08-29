import cartopy.crs as ccrs
from cartopy.io.img_tiles import OSM
import matplotlib.pyplot as plt
import pandas as pd
osm_tiles = OSM()

# Usamos la proyección de OSM.
ax = plt.axes(projection=osm_tiles.crs) 
ax.set_extent([6,-20, 26, 45])
ax.add_image(osm_tiles, 7)
df = pd.read_csv ('terremotos_esp_1370-2024.csv', sep=';', low_memory=False)

for i in range(0,len(df)):
    ax.plot(df['    Longitud'][i], df['     Latitud'][i], color='red', linewidth=0.05,marker='+',transform=ccrs.Geodetic(), alpha = 0.1) 
    # alpha para la transparencia

plt.show()
