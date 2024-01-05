from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_SauceDemo:
    # Chrome tarayıcısını başlat
        driver = webdriver.Chrome()
        
        # Google ana sayfasına git
        driver.get("https://www.saucedemo.com")
        
        # Tarayıcı penceresini maksimum boyuta getir
        driver.maximize_window()
        
        # 3 saniye bekle
        sleep(3)
        
        # Kullanıcı adı ve şifre girişi
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        sleep(3)
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")  # Şifrenizi buraya girin
        sleep(3)

        loginButton = driver.find_element(By.ID,"login-button")
        loginButton.click()
        sleep(5)   
        errorMessage= driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/h3")
        testResult = errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        print(f"Test sonucu: {testResult}")

testClass = Test_SauceDemo()
testClass.test_invalid_login()
