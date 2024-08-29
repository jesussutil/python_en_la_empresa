import ssl
from ldap3 import Server, Connection, SAFE_SYNC, Tls, ALL
 
username = "foo"
passwd = "contraseña"
host = "192.168.1.100" # IP del directorio de pruebas.

server = Server(host,tls=Tls(),get_info = ALL)
conn = Connection(server, 'cn='+username+',OU=users,DC=empresa,DC=com', passwd)
print("Antes del bind:\n", conn) # Podemos ver que no hay socket levantado

conn.start_tls()
print("TLS iniciado:\n", conn)
conn.bind()
print("Después del bind:\n", conn) # ahora ya está la comunicación establecida

## ---- segunda parte

print(conn.entries) # aquí no hay nada porque no hemos buscado nada

result= conn.search('DC=empresa,DC=com', f'(sAMAccountName={username})', attributes=["givenName", "sn", "mail","memberOf"])

if (result):
    print(conn.entries) # Mostramos la información recuperada
