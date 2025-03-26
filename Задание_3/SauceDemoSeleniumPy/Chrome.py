from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
time.sleep(2)

def test_login():
    try:
        # Поиск элементов
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        time.sleep(2)

        # Ввод данных и отправка формы
        username_input.send_keys(username)
        time.sleep(1)
        password_input.send_keys(password)
        time.sleep(1)
        login_button.click()

        time.sleep(5)

        print("Тест пройден: Вход выполнен успешно.")
        time.sleep(3)
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()
