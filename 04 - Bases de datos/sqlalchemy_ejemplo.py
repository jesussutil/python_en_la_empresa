import sqlalchemy
from sqlalchemy import create_engine, select, MetaData, Table, Column

# engine = sqlalchemy.create_engine('dialect+driver://usuario:password@host/dbname')
engine = sqlalchemy.create_engine('mysql+mysqlconnector://user:passwd@localhost:3306/tb', echo=True)

# Cargamos la estructura de la base de datos
metadata = sqlalchemy.MetaData()
metadata.reflect(bind=engine)

# apunto a la tabla pois con todas sus columnas.
table = metadata.tables["pois"]

query= sqlalchemy.select(table).where(table.columns.tipo == 'museo')

# Ejecutamos la consulta
with engine.connect() as connection:
    results = connection.execute(query).fetchall()

# Usamos los resultados obtenidos para nuestro propósito.
for result in results:
    print(result)
