import pandas as pd
import matplotlib.pyplot as plt

rollingstone = pd.read_csv("rollingstone.csv", delimiter=";")

df = rollingstone.groupby(['Year'])['Year'].count().reset_index(name='counts')
ax = df.plot(kind='bar',x='Year',y='counts', xlabel='Año', ylabel='Canciones en Top500', title='Top 500 RollingStone 2021',ylim=[0, 25])

# hacemos pequeños cambios sobre el gráfico por defecto
# añadimos el texto 1971 Rocks!
ax.text(22, 21, '1971 Rocks!', color='red', fontsize=15, fontweight='bold') 

# mostramos únicamente las líneas horizontales
ax.grid(axis = 'y') 

# eliminamos la leyenda
ax.get_legend().remove() 

plt.show()
