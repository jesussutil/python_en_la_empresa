from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()    
driver.get("https://www.google.com")    

try: 
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH,"//button[contains(.,'Acept')]")))
        
    driver.find_element(by=By.XPATH,value="//button[contains(.,'Acept')]").click()

except:
    print (">>> ERROR")

# Almacenamos en lista_busqueda todas las búsquedas a realizar
lista_busqueda = open('palabras_clave.txt', 'r',encoding = "utf-8")
lista = lista_busqueda.readlines()
print (lista)
lista_busqueda.close

timestamp = time.time()

df = pd.DataFrame()
df['posicion'] = None
df['busqueda'] = None
df['url'] = None
df['titulo'] = None
df['extracto'] = None
df['resultados'] = None
df['timestamp'] = None

# Iteramos sobre el listado de búsqueda
for a_buscar in lista:
    url="https://www.google.com/search?q="+a_buscar.replace(' ','+').rstrip('\n')+"&num=100"
    print (url)
    driver.get(url)

    driver.find_element(By.XPATH,"//div[@id='hdtb-tls']").click()
   
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH,"//div[@id='result-stats']")))
        
    resultados = driver.find_element(By.XPATH,"//div[@id='result-stats']").text 
    cabeceras=driver.find_elements(By.XPATH,'//div[@id="search"]//div[@data-snhf="0"]//h3')
    
    url = driver.find_elements(By.XPATH, '//div[@id="search"]//div[@data-snhf="0"]//a//h3/ancestor::a')
    contenidos=driver.find_elements(By.XPATH,'//div[@id="search"]//div[@data-sncf="1"]')

    for i in range(len(cabeceras)): # Iteramos sobre los resultados
        position = i +1
        df_add = pd.DataFrame.from_records({
        'posicion': ''+str(position)+'',
        'busqueda':''+str(a_buscar.rstrip('\n'))+'',
        'url':''+str(url[i].get_attribute("href"))+'', 
        'titulo':''+str(cabeceras[i].text)+'',
        'extracto': ''+str(contenidos[i].text)+'', 
        'resultados':''+str(resultados)+'',
        'timestamp':''+str(timestamp)+''}, index=[0])
        df = pd.concat([df, df_add], ignore_index=True)
        print (df)
        
df.to_csv(r'para_mi_estudio_de_mercado.csv', sep =';', encoding = "utf-8", index = False)
