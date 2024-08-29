import pandas as pd
import matplotlib.pyplot as plt

trends=pd.read_csv("trends.csv", header=1,encoding = "ISO-8859-1")

# Se elimina el '<' de todo el dataframe
trends=trends.replace('<','',regex=True) 

trends['iphone: (Todo el mundo)']=trends['iphone: (Todo el mundo)'].astype(float)
trends['iPhone: (Todo el mundo)']=trends['iPhone: (Todo el mundo)'].astype(float)

# se establecen estos colores para las gráficas
colores = ['#2196f3']+['#f44336']+['#ffca28'] 
ax = trends.plot(kind='line',x='Mes',ylim=[0, 100], color=colores)

# se establecen esos valores para el eje Y.
ax.set_yticks([0, 25, 50, 75, 100]) 
ax.tick_params(axis='x', colors='#9e9e9e')

# se ocultan las marcas en el eje Y.
ax.tick_params(axis='y', left=False, colors='#9e9e9e') 
ax.spines['bottom'].set_color('#9e9e9e')
ax.spines.left.set_visible(False)  # se oculta la parte izquierda del recuadro
ax.spines.right.set_visible(False) # se oculta la parte derecha del recuadro
ax.spines.top.set_visible(False)   # se oculta la parte superior del recuadro

ax.grid(axis = 'y',which='major', color="#d3d3d3")
plt.show()
