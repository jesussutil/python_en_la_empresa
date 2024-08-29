from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import logging
import time

url = "https://www.google.es/maps/"
input = "input.txt"     # Archivo con direcciones a convertir en lat/long

options = webdriver.ChromeOptions()
# Modo "silencioso" para evitar mensajes inoportunos.
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get(url)         # Cargamos la url

# Esperamos al popup de las cookies y lo aceptamos.
try:
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH,"//span[contains(.,'Acept')]")))
    
    driver.find_element(by=By.XPATH, value="//span[contains(.,'Acept')]").click()

except:
    print (">>> ERROR cargando Google Maps")
    exit()

# Comprobamos si ya se ha cargado comprobando que la búsqueda es visible
try:
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located
    ((By.XPATH, "//input[@id='searchboxinput']")))
	
except:
    print (">>> ERROR cargando Google Maps")
    exit()

## -- aquí empieza la parte 2.

# leemos el fichero con las direcciones a buscar
direcciones = open(input, 'r')
dirlist = direcciones.readlines()
direcciones.close
maxdirs=len(dirlist)

# usamos el módulo logging para almacenar el resultado
logfile = "log_"+str(datetime.now()).replace(" ", "_").replace(":", "_") +".csv"
logging.basicConfig(filename=logfile, format='%(message)s', level=logging.INFO)
logging.info("direccion;lat;long")           # añadimos esta cabecera al csv

# iteramos en el listado de direcciones que hemos leído desde el archivo
for dir in dirlist:

    urlafter = ""
    estado = ""	
	
    driver.get(url)                 # volvemos al estado inicial

    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH,"//input[@id='searchboxinput']")))	

    in_dir = driver.find_element(by=By.ID, value="searchboxinput")
    in_dir.clear()
    in_dir.send_keys(dir)

    try:
        in_dir.send_keys(Keys.ENTER)
    except:
        driver.find_element_by_xpath("//button[@id='searchbox-searchbutton']").click()        

    wait = WebDriverWait(driver, 10)
    wait.until(ec.url_contains("@")) # Esperamos a que aparezca una @ en la url
	
    urlafter = driver.current_url

    try:
        lat = urlafter.split('@')[1].split(',')[0]
        long = urlafter.split('@')[1].split(',')[1]
    except:
        lat = ""
        long = ""
				
    detail= dir.rstrip('\n')+";"+lat+";"+long
    logging.info(detail)

