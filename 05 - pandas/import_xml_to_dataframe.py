import pandas as pd

df = pd.read_xml ('archivo.xml', encoding = "ISO-8859-1")
df=df[['FECHA','ID_PEDIDO','PRECIO']]
