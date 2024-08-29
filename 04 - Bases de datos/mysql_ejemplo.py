import pymysql

# Información de la conexión
host = 'localhost'  
db = 'mibdd'  
usuario = 'user'  
passwd = 'contraseña'

# Se inicia la conexión a la base de datos
conector = pymysql.connect(host=host, port=3306, user=usuario, passwd=passwd, db=db,charset="utf8")

# Creamos un cursor
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
