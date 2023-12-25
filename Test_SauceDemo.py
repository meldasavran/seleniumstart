from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Test_SauceDemo:
    def test_invalid_login(self):
        # ChromeDriver'ı otomatik olarak yönetmek için webdriver_manager kullan
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        
        # Google ana sayfasına git
        driver.get("https://saucedemo.com")
        
        # Tarayıcı penceresini maksimum boyuta getir
        driver.maximize_window()
        
        # 3 saniye bekle
        sleep(3)
        
        # Kullanıcı adı ve şifre girişi
        usernameInput = driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("secret_sauce")
        
        passwordInput = driver.find_element(By.ID, "password")
        passwordInput.send_keys("your_password")  # Şifrenizi buraya girin
        
testClass = Test_SauceDemo()
testClass.test_invalid_login()
