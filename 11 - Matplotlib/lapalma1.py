import rasterio
from rasterio.windows import Window
import numpy as np
import matplotlib.pyplot as plt

with rasterio.open('eu_dem_v11_E10N10.TIF') as src:
    array = src.read(1, window=Window(23500, 34250, 1500, 1800))

#plt.imshow(array, cmap='terrain',vmin=0) 
plt.imshow(array, cmap='inferno')
#plt.imshow(array, cmap='inferno', vmin=0)
#plt.imshow(array, cmap='inferno', norm='log')
plt.show()
