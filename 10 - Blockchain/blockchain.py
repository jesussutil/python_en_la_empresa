import hashlib, sys, random, time

# creamos una clase a la que le pasamos unos datos (cebador)
class micadenadebloques: 
                         # y el hash de unos datos previos (semilla)
    def __init__(self, hash_previo, datos):

self.hash_previo = hash_previo
self.datos = datos

self.block_data = "{'data':'"+str(datos[0])+"';'timestamp':'"+str(datos[1])+"';'hash_previo':'"+str(hash_previo)+"'}"
self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

# Esta semilla con la que se genera el primer bloque.        
semilla = hashlib.sha256(str(random.randint(1,1000000000000)).encode('utf-8')).hexdigest()
cebador = ["primer bloque",str(time.time())]
bloque = micadenadebloques(semilla, cebador)

print("datos: "+ bloque.block_data)
print("hash: "+ bloque.block_hash)
print ("---------------")
print ("escribe el contenido del siguiente bloque y pulsa intro")
bloque = micadenadebloques(bloque.block_hash, [line.strip(),str(time.time())])

for line in sys.stdin:
    print ("---------------")   
    print("datos: "+ bloque.block_data)
    print("hash: "+ bloque.block_hash)
    print ("## escribe el contenido del siguiente bloque y pulsa intro")
