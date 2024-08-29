import rasterio
from rasterio.windows import Window
import numpy as np

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

with rasterio.open('eu_dem_v11_E10N10.TIF') as src:
    Z = src.read(1, window=Window(23500, 34250, 1500, 1800))

Z[(Z < -1)] = 0

x = np.arange(0,1500,1)
y = np.arange(0,1800,1)

# meshgrid crea un grid rectangular a partir de dos arrays lineales. 
X,Y = np.meshgrid(x,y) 

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(projection='3d')

# se pondera el eje Z para que el aspecto de la isla sea proporcional
ax.set_zlim3d(0,15000) 

ax.plot_surface(Y, X, Z, cmap="terrain", rstride=10, cstride=10)
plt.show()         
