from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time

#Hansel Perez 25-0461

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

# Iniciar la sesión de Appium
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(2)

# Realizar una suma: 7 + 3
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "7").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "más").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "igual a").click()

time.sleep(2)

# Capturar el resultado
result = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final").text
print(f"Resultado de la suma: {result}")


driver.quit()
