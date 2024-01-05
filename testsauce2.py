
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.action_chains import ActionChains


class testsaucedemo2:
    def test_invalid_login(self):
        driver=webdriver.Chrome()
        driver.get("https://saucedemo.com")
        driver.maximize_window()

        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(By.ID, "user-name"))


        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("locket_out_user")
        
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("secret_sauce")  # Şifrenizi buraya girin

        loginButton=driver.find_element(By.ID, "login-button")
        loginButton.click()

