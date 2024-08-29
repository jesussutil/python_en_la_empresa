import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas as pd

eq = pd.read_csv ('earthquakes1970-2014.csv', sep=',')

ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

eq.plot(ax=ax, kind='hexbin', x='Longitude', y='Latitude', gridsize=40, cmap='Reds')

plt.show()
