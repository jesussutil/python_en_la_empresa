import sqlalchemy
from sqlalchemy import create_engine, select, MetaData, Table, Column, text

# engine = sqlalchemy.create_engine('dialect+driver://usuario:password@host/dbname')
engine = sqlalchemy.create_engine('mysql+mysqlconnector://user:passwd@localhost:3306/tb', echo=True)

# Cargamos la estructura de la base de datos
metadata = sqlalchemy.MetaData()
metadata.reflect(bind=engine)

# Ejecutamos la consulta
with engine.connect() as connection:
    results = connection.execute(text("SELECT * FROM pois WHERE tipo = 'museo'"))

# Usamos los resultados obtenidos para nuestro propósito.
for row in results:
    print(row)
