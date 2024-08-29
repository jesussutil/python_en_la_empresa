import pymysql
import pandas as pd

host,username,pass = 'mysql.host','usuario', 'contraseña'

query = "SELECT * from datos"

con = pymysql.connect(host=host, user=username, password=pass, database="test")

df = pd.read_sql(query, con) # Almacenamos en un dataframe el resultado
