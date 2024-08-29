import pandas as pd
import matplotlib.pyplot as plt

temp=pd.read_csv("https://www.aemet.es/es/serviciosclimaticos/datosclimatologicos/valoresclimatologicos_la-palma-aeropuerto.csv?l=C139E&k=coo", header=1, encoding = "ISO-8859-1")

ax = temp.plot(kind='bar',x='Mes',y='T', xlabel='Mes/Año', ylabel='Temperatura ºC',ylim=[15, 25])
plt.xticks(rotation = 0)
plt.show()
