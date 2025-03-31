from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

# Configuración de Appium
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:deviceName": "c5e904a0b49f",  
    "appium:automationName": "UiAutomator2",
    "appium:newCommandTimeout": 3600
})

print("Iniciando sesión en Appium...")
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(2)

print("Abriendo Calculadora...")
driver.activate_app("com.google.android.calculator")
time.sleep(2)

print("Realizando operación en la calculadora...")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "7").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "más").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "igual a").click()

result = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final").text
print(f"Resultado de la suma: {result}")
time.sleep(2)

# **SEGUNDA PRUEBA: Abrir Google Chrome**
print("Regresando a pantalla principal...")
driver.press_keycode(3) 
time.sleep(2)

print("Abriendo Google Chrome...")
chrome_icon = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome")
chrome_icon.click()
time.sleep(5)  


driver.quit()
print("Prueba finalizada con éxito.")
