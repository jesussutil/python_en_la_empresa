from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import socket, json, time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime

# los métodos getip() y json_validator(data) se han incorporado en meth.py
import meth 

url = "https://www.google.es/maps/"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get(url)

try:
wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH,"//span[contains(.,'Acept')]")))
    
driver.find_element(by=By.XPATH,value="//span[contains(.,'Acept')]").click()
print (">>> Click en acepto")
    
except:
    print (">>> ERROR cargando Google Maps")
    exit()

try:
wait = WebDriverWait(driver, 10)
wait.until(ec.visibility_of_element_located ((By.XPATH,"//input[@id='searchboxinput']")))
    
print (">>> Ya se ha cargado google maps")

except:
    print (">>> ERROR cargando Google Maps")
    exit()

def getlatlong(addr, driver):

urlafter,estado,recv = "","",""
    
driver.get(url)                 # volvemos al estado inicial
wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH,"//input[@id='searchboxinput']")))	
time.sleep(1)

in_dir = driver.find_element(by=By.ID,value="searchboxinput")
in_dir.clear()
in_dir.send_keys(addr)

    try:
        in_dir.send_keys(Keys.ENTER)
    except:
   driver.find_element(by=By.XPATH,value="//button[@id='searchbox-searchbutton']").click()

    wait = WebDriverWait(driver, 10)
    wait.until(ec.url_contains("@"))
    
    urlafter = driver.current_url
    
    print(urlafter)
    
    try:
        lat = urlafter.split('@')[1].split(',')[0]
        long = urlafter.split('@')[1].split(',')[1]

    except:
        lat,long = "",""
    
    return lat,long

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'No se acepta metodo GET')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        
        valid = meth.json_validator(body) # Valido json recibido.
        
        if (valid == True):
            recv = json.loads(body)
            addr = recv['address']
            print ("direccion: ", addr)
            lat,long = getlatlong(addr, driver)

            self.send_response(200)
            self.end_headers()
            response = BytesIO()
            response.write(str.encode(lat)+b','+str.encode(long)+b'\n')       	
            self.wfile.write(response.getvalue())
            
        else:
            self.send_response(400)
            self.end_headers()
            response = BytesIO()
            response.write(b'400 BAD REQUEST \n')            
            response.write(b'This POST does not contains a valid Json. \n')
            response.write(b'Received: ')
            response.write(body)
            response.write(b'\n')           
            self.wfile.write(response.getvalue()) 

myip = meth.getip()	

httpd = HTTPServer((myip, 8001), SimpleHTTPRequestHandler)
httpd.serve_forever()
