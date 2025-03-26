from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

# Настройки
URL = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(URL)
driver.maximize_window()
time.sleep(2)

def test_login():
    driver.find_element(By.ID, "user-name").send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory.html" in driver.current_url, "Не удалось войти в систему!"
    print("Тест пройден: Вход выполнен успешно.")

    time.sleep(2)
    driver.quit()
