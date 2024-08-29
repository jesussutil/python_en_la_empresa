import pandas as pd

df = pd.read_json ('archivo.json', dtype=str, encoding = "ISO-8859-1")
df=df[['FECHA','ID_PEDIDO','PRECIO']]
