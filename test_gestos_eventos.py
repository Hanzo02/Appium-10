from appium import webdriver
from appium.options.common.base import AppiumOptions
import time

# Configuración de Appium
options = AppiumOptions()
options.load_capabilities({
    "platformName": "Android",
    "appium:deviceName": "c5e904a0b49f",  
    "appium:automationName": "UiAutomator2",
    "appium:appPackage": "com.google.android.calculator",
    "appium:appActivity": "com.android.calculator2.Calculator",
    "appium:newCommandTimeout": 3600
})

print("Iniciando sesión en Appium...")
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(2)
print("Calculadora abierta correctamente.")

# Realizar un deslizamiento de abajo hacia arriba
print("Realizando deslizamiento...")
driver.swipe(500, 1500, 500, 500, 800)
time.sleep(2)

print("Deslizamiento completado.")

driver.quit()
print("Prueba finalizada con éxito.")
