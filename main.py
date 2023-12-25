# Selenium'dan webdriver ve By modüllerini, webdriver_manager'dan ChromeDriverManager'ı ve time modülünden sleep fonksiyonunu içe aktar
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Chrome tarayıcısını başlat
driver = webdriver.Chrome()

# Google ana sayfasına git
driver.get("https://www.google.com")

# Tarayıcı penceresini maksimum boyuta getir
driver.maximize_window()

# 3 saniye bekle
sleep(3)

# 'q' adlı elemanı bul ve içine "annem seni seviyorum" yaz
input = driver.find_element(By.NAME, "q")
input.send_keys("annem seni seviyorum")

# 2 saniye bekle
sleep(2)

# 'btnK' adlı elemanı bul ve tıkla (Google'da arama yap)
searchButton = driver.find_element(By.NAME, "btnK")
searchButton.click()

# 2 saniye bekle
sleep(2)

# Belirli bir XPath ile bir elemanı bul ve tıkla
sonuc = driver.find_element(By.XPATH, "//*[@id='iur']/div/div/div/div[1]/div[2]/a/div[1]/div")
sonuc.click()

# 3 saniye bekle
sleep(3)


