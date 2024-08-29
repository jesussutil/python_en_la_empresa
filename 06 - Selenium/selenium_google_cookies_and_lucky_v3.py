from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()             
driver.get("https://www.google.com")    

try: 
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located
    ((By.XPATH,"//button[contains(.,'Acept')]")))
    
    driver.find_element(by=By.XPATH,value="//button[contains(.,'Acept')]").click()

except:
    print (">>> ERROR")

botones = driver.find_elements(By.XPATH,"//input[@value='Voy a tener suerte']")

try:
    wait = WebDriverWait(driver, 10)         
    wait.until(ec.visibility_of_element_located(
    (By.XPATH,"//input[@title='Buscar']")))
    
    campo_busqueda = driver.find_element(By.XPATH,"//input[@title='Buscar']")
    campo_busqueda.clear()
    campo_busqueda.send_keys("python")
    
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable(botones[0]))
    botones[0].click()   

except:
    print (">>> Error en la búsqueda")
