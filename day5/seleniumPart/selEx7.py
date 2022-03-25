from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('http://www.danawa.com')
time.sleep(3)

from selenium.webdriver.common.action_chains import ActionChains

def mouseOverElement(title):
    element = driver.find_element(By.LINK_TEXT, title)
    ActionChains(driver).move_to_element(element).perform()
    return element

mouseOverElement('가전·TV')
mouseOverElement('TV')
mouseOverElement('QLED/나노셀TV')
mouseOverElement('QLED TV').click()

driver.quit()