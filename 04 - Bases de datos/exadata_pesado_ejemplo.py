import oracledb

# Información de la conexión
host = 'nombre_del_host'
username = 'tu_usuario'
password = 'tu_contraseña'
instant_client_dir = r"C:\Oracle\instantclient_21_13" # ruta donde está instalado.

# Inicializamos el modo pesado
oracledb.init_oracle_client(lib_dir=instant_client_dir) 

# Se inicia la conexión a la base de datos
conector = oracledb.connect(user=username, password=password, dsn=host)

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
