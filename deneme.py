from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Tarayıcıyı headless (gizli) modda başlatmak için seçenekler
options = Options()
options.add_argument('--headless')  # Tarayıcıyı gizli modda çalıştırır.
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

# WebDriver'ı başlatıyoruz
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("Tarayıcı başlatılıyor...")
    # Web sitesini açıyoruz
    driver.get("https://trgoals1229.xyz/")

    # Sayfa tamamen yüklendiği için bir süre bekliyoruz
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Sayfa yüklendikten sonra bekle
    
    # Şu anki URL'yi alıyoruz
    current_url = driver.current_url
    print(f"Açılan URL: {current_url}")

    # URL'yi ana_link.txt dosyasına yazıyoruz
    with open("ana_link.txt", "w") as file:
        file.write(current_url)  # URL'yi dosyaya yazıyoruz.

    print("Açılan URL 'ana_link.txt' dosyasına kaydedildi.")

except Exception as e:
    print(f"Hata oluştu: {e}")

finally:
    driver.quit()  # Tarayıcıyı kapatıyoruz
