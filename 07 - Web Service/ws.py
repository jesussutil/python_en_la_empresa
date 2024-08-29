from http.server import HTTPServer, BaseHTTPRequestHandler
import socket
import json

def getip():                   # método para obtener la ip pública por defecto
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 53))
ip = s.getsockname()[0]
s.close()
return (ip)

def json_validator(data):      # método que valida si un json tiene buen formato
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):      # Ante un GET respondemos que no se acepta con un 405
        self.send_response(405)
        self.end_headers()
        self.wfile.write(b'No se acepta método GET')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        
        valid = json_validator(body)       # Valido el json recibido.
        
        if (valid == True):                # Si es correcto devolvemos un 200

            valid = False

            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            response.write(b'El POST contiene un JSON válido.\n')
            response.write(b'Received: ')
            response.write(body)
            response.write(b'\n')           			
            self.wfile.write(response.getvalue())
            
        else:                              # Si es incorrecto devolvemos un 400
            self.send_response(400) 
            self.end_headers()
            response = BytesIO()
            response.write(b'400 BAD REQUEST \n')            
            response.write(b'El POST NO contiene un JSON válido. \n')
            response.write(b'Recibido: ')
            response.write(body)
            response.write(b'\n')           
            self.wfile.write(response.getvalue()) 

myip = getip()	                       # Obtengo la IP pública     

httpd = HTTPServer((myip, 8001), SimpleHTTPRequestHandler)
httpd.serve_forever()
