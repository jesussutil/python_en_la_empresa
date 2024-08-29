import hashlib, sys, random, time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv ('loteria.csv', sep=';', dtype=str,usecols= ['Año','Número','Vendido en'])
df["terminación"] = ""
df["decena"] = ""

for i in df.index:
    df['decena'][i]=df['Número'][i][3:4]
    df['terminación'][i]=df['Número'][i][4:5]

sns.jointplot(x='decena', y='terminación', data=df)

plt.show()
