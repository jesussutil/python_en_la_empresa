from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()             # levantamos una instancia del navegador
driver.get("https://www.google.com")    # le pedimos que vaya a www.google.com

# intentamos esto, y si no pudiera ejecutarlo saldría por el except.
try: 
# Esperamos 10 segundos al popup de las cookies y hacemos clic en botón de aceptar.
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located
    ((By.XPATH,"//button[contains(.,'Acept')]")))
    
    driver.find_element(by=By.XPATH,value="//button[contains(.,'Acept')]").click()

except:
    print (">>> ERROR")
