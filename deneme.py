from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
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

    # Sayfa tamamen yüklendiği için kısa bir süre bekliyoruz
    time.sleep(3)
    
    # Şu anki URL'yi alıyoruz
    current_url = driver.current_url
    print(f"Açılan URL: {current_url}")

    # URL'yi ana_link.txt dosyasına yazıyoruz
    with open("ana_link.txt", "w") as file:
        file.write(current_url)  # URL'yi dosyaya yazıyoruz.

    print("Açılan URL 'ana_link.txt' dosyasına kaydedildi.")

finally:
    driver.quit()  # Tarayıcıyı kapatıyoruz
