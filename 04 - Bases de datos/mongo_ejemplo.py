import pymongo

# Información de la conexión
usuario = "mi_usuario" 
passwd= "mi_contraseña_secreta"
host = "ip_de_mi_base_de_datos" # por ejemplo "mongodb://localhost:27017"
db= "base_de_datos_a_usar" 

# Se inicia la conexión a la base de datos
conexion = pymongo.MongoClient(host, username=username, password=passwd)

mydb = conexion[db]
mycol = mydb["my_coleccion"]

# Consulta
myquery = {"max": 0} # ¡En formato JSON!

# Ejecutamos la consulta
mydoc= mycol.find(myquery)

# Aquí usamos los resultados obtenidos para nuestro propósito.
for i in mydoc:
    print(i)

# Finalmente, cerramos la conexión
conexion.close()
