from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Selenium ile tarayıcıyı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Sayfayı aç
driver.get("https://trgoals1234.xyz/")
time.sleep(5)  # Sayfanın tamamen yüklenmesi için bekle

# Tüm script içeriklerini al
scripts = driver.find_elements("tag name", "script")
with open("baseurl.txt", "w", encoding='utf-8') as f:
    for script in scripts:
        script_content = script.get_attribute('innerHTML')
        if script_content:  # Boş içerik olanları yazma
            f.write(script_content + "\n")  # Her script'ten sonra yeni satır

# Tarayıcıyı kapat
driver.quit()
