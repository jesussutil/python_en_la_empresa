import pyodbc

# Información de la conexión
host = 'localhost'  
db = 'mibdd' 
usuario = 'user'  
passwd = 'contraseña'  

# Se inicia la conexión a la base de datos
conector = pyodbc.connect('DRIVER={MySQL ODBC 8.3 Unicode Driver}; SERVER=' + host +'; DATABASE=' + db+ '; UID=' + usuario + '; PWD=' + passwd)

cursor = conector.cursor()
# Consulta
consulta = "SELECT * FROM mi_tabla"

# Ejecutamos la consulta
cursor.execute(consulta)

resultados = cursor.fetchall()

# Mostramos los resultados
for fila in resultados:
    print(fila)
# Finalmente, cerramos la conexión
conector.close()
