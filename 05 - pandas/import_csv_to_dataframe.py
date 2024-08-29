import pandas as pd
 
df = pd.read_csv ('archivo.csv', sep=';', dtype=str, encoding = "ISO-8859-1",usecols= ['FECHA','ID_PEDIDO','PRECIO'])
