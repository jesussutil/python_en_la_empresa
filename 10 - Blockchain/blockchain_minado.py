import hashlib, sys, random, time

class micadenadebloques:
    
    def __init__(self, hash_previo, datos):

self.hash_previo = hash_previo
self.datos = datos

self.block_data = "{'data':'"+str(datos[0])+"';'timestamp':'"+str(datos[1])+"';'nonce':'"+str(datos[2])+";'hash_previo':'"+str(hash_previo)+"'}"
self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
cadena = ["primer bloque",str(time.time()),"0"]
semilla = hashlib.sha256(str(random.randint(1,1000000000000)).encode('utf-8')).hexdigest()

bloque = micadenadebloques(semilla, cadena)

print("datos: "+ bloque.block_data)
print("hash: "+ bloque.block_hash)
print ("---------------")
print ("## escribe el contenido del siguiente bloque y pulsa intro")

for line in sys.stdin:
    print ("---------------")
    nonce=0
    # validamos que el primer carácter del hash sea un cer0.
    while(True): 
bloque_temp = micadenadebloques(bloque.block_hash, [line.strip(),str(time.time()), nonce])
#Aumentamos el nonce hasta encontrar un hash que cumpla la condición.
nonce=nonce+1 
if (str(bloque_temp.block_hash).startswith('0', 0)):
    bloque=bloque_temp
            break
    
    print ("iteraciones: "+str(nonce))
    print("datos: "+ bloque.block_data)
    print("hash: "+ bloque.block_hash)
    print ("## escribe el contenido del siguiente bloque y pulsa intro")
