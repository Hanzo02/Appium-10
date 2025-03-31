from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

# Configuración de Appium para Google Chrome
options_hybrid = AppiumOptions()
options_hybrid.load_capabilities({
    "platformName": "Android",
    "appium:deviceName": "c5e904a0b49f",  
    "appium:automationName": "UiAutomator2",
    "browserName": "Chrome",
    "appium:newCommandTimeout": 3600
})

# Iniciar sesión en Appium
driver = webdriver.Remote("http://127.0.0.1:4723", options=options_hybrid)
time.sleep(3)

driver.get("https://www.w3schools.com/html/html5_video.asp")
time.sleep(3)

contexts = driver.contexts
print(f"Contextos disponibles: {contexts}")

for context in contexts:
    if "WEBVIEW" in context:
        driver.switch_to.context(context)
        print(f"Cambiado al contexto: {context}")
        break

time.sleep(3)

# Volver al contexto nativo
driver.switch_to.context("NATIVE_APP")
print("Regresando al contexto nativo.")

driver.quit()
