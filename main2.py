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

# 'q' adlı elemanı bul ve içine "kodlamaio" yaz
input = driver.find_element(By.NAME, "q")
input.send_keys("kodlamaio")

# 2 saniye bekle
sleep(2)

# 'btnK' adlı elemanı bul ve tıkla (Google'da arama yap)
searchButton = driver.find_element(By.NAME, "btnK")
searchButton.click()

# 2 saniye bekle
sleep(2)

# Belirli bir XPath ile bir elemanı bul ve tıkla
sonuc = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3")
sonuc.click()

# 3 saniye bekle
sleep(3)

# Sayfadaki tüm "course.listing" sınıfına sahip elemanları bul
listOfcourses = driver.find_elements(By.CLASS_NAME, "course.listing")
# Sayfadaki tüm "course.listing" sınıfına sahip elemanları bul
# By.CLASS_NAME: Bu, Selenium'un bir öğe bulmak için kullanılan stratejilerden biridir. Bu strateji, bir HTML öğesini bulmak için sınıf adını kullanır.
# "course.listing": Bu, aranan öğelerin sınıf adıdır. Yani, course.listing sınıfına sahip tüm HTML öğelerini bulmak istiyoruz.
# driver.find_elements(...): Bu, tarayıcıda bulunan tüm öğeleri bulmaya yönelik bir Selenium fonksiyonudur. find_elements kullanıldığında, eğer hiç öğe bulunmazsa boş bir liste döner.
# Bu satırın amacı, sayfadaki tüm course.listing sınıfına sahip öğeleri bulup, bu öğeleri listOfcourses adlı bir liste içinde depolamaktır.
# Bu öğeler daha sonra başka işlemler için kullanılabilir, örneğin, bu öğelerin sayısını kontrol ederek bir test senaryosu oluşturabilir veya bu öğeler üzerinde döngü kullanarak her bir öğe ile ilgili işlemler gerçekleştirilebilir.



# Test sonucunu hesapla (listOfcourses'in uzunluğu 6 ise True, değilse False)
testResult = len(listOfcourses) == 6
print(f"Test sonucu: {testResult}")
