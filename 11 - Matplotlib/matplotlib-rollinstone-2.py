import pandas as pd
import matplotlib.pyplot as plt

rs = pd.read_csv("rollingstone.csv", delimiter=";")

# Así agrupamos por artista para ver quien tiene más canciones en el top 500
df=rs.groupby(['Artist']).size().reset_index(name = 'counts').sort_values('counts')

# nos quedamos con los mayores y los ordenamos de forma descendente (por defecto es ascendente)
df = df[df.counts > 2].sort_values('counts', ascending=False).reset_index(drop = True)

colores = ['red'] + ['blue'] * len(df)

ax = df.plot(kind='barh', x='Artist', y='counts', color=colores)

ax.get_legend().remove()
ax.invert_yaxis()

plt.show()
