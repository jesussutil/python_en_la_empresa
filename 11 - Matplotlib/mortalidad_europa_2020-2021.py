import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import numpy as np

mortality_euromomo = pd.read_csv ('charts-pooled-by-age-group.csv', sep=';', dtype=str)

mortality0to14 = mortality_euromomo [(mortality_euromomo ["group"] == "0to14")]
mortality65P = mortality_euromomo [(mortality_euromomo ["group"] == "65P")]
mortality = mortality_euromomo [(mortality_euromomo ["group"] == "Total")]

# Usamos gridspec para distribuir los subplots facilmente
gs = gridspec.GridSpec(2, 2) 
fig = plt.figure()

# Gráfico 1
ax1 = fig.add_subplot(gs[0, 0]) # fila 0, columna 0

mortality0to14 = mortality0to14.astype({'Low normal range':'float','High normal range':'float','Observed count':'float'})

ax1.plot(mortality0to14['week'], mortality0to14['Low normal range'], '-', linewidth=0)
ax1.plot(mortality0to14['week'], mortality0to14['High normal range'], '-', linewidth=0)
ax1.plot(mortality0to14['week'], mortality0to14['Observed count'], '-', linewidth=1)

ax1.fill_between(mortality0to14['week'], mortality0to14['High normal range'],mortality0to14['Low normal range'], where=mortality0to14['High normal range'] >= mortality0to14['Low normal range'], facecolor='grey', alpha=0.2, interpolate=True)

plt.xticks (np.arange(0, 110, 20),rotation=0)
plt.title("Mortalidad en menores de 14")

# Gráfico 2
ax2 = fig.add_subplot(gs[0, 1]) # fila 0, columna 1

mortality65P = mortality65P.astype({'Low normal range':'float','High normal range':'float','Observed count':'float'})

ax2.plot(mortality65P['week'], mortality65P['Low normal range'], '-', linewidth=0)
ax2.plot(mortality65P['week'], mortality65P['High normal range'], '-', linewidth=0)
ax2.plot(mortality65P['week'], mortality65P['Observed count'], '-', linewidth=1)

ax2.fill_between(mortality65P['week'], mortality65P['High normal range'],mortality65P['Low normal range'], where=mortality65P['High normal range'] >= mortality65P['Low normal range'], facecolor='grey', alpha=0.2, interpolate=True)

plt.xticks (np.arange(0, 110, 20),rotation=0)
plt.title("Mortalidad en mayores de 65")

# Gráfico 3
ax3 = fig.add_subplot(gs[1, :]) # fila 1, todas las columnas

mortality = mortality.astype({'Low normal range':'float','High normal range':'float','Observed count':'float'})

ax3.plot(mortality['week'], mortality['Low normal range'], '-', linewidth=0)
ax3.plot(mortality['week'], mortality['High normal range'], '-', linewidth=0)
ax3.plot(mortality['week'], mortality['Observed count'], '-', linewidth=1, label="Total")

ax3.plot(mortality65P['week'], mortality65P['Observed count'], '--', linewidth=1, label=">65 años")

ax3.fill_between(mortality['week'], mortality['High normal range'],mortality['Low normal range'], where=mortality['High normal range'] >= mortality['Low normal range'], facecolor='grey', alpha=0.2, interpolate=True)

plt.legend(loc="upper right")
plt.xticks (np.arange(0, 110, 10),rotation=0)
plt.title("Mortalidad Total + mayores de 65")
plt.show()
