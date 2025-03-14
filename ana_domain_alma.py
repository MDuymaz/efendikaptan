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

    # Ana link dosyasındaki URL'yi okuyoruz
    with open("ana_link.txt", "r") as file:
        url = file.read().strip()

    # URL'yi kullanarak web sitesini açıyoruz
    driver.get(url)

    # Sayfa tamamen yüklendiği için kısa bir süre bekliyoruz
    time.sleep(3)

    # Şu anki URL'yi alıyoruz
    current_url = driver.current_url
    print(f"Açılan URL: {current_url}")

    # Ana link dosyasını okuyup eski URL'yi kontrol edelim
    with open("ana_link.txt", "r") as file:
        old_url = file.read().strip()

    # Eğer eski URL ile yeni URL farklıysa, dosyayı güncelleyelim
    if current_url != old_url:
        print(f"URL değişti. Yeni URL: {current_url}")

        # Eğer yeni URL "giriş" içeriyorsa, "1230" sayısını bir artır
        if 'giris' in current_url:
            base_url = "https://trgoals"
            updated_number = int(old_url.split('trgoals')[1].split('.')[0]) + 1
            new_url = f"{base_url}{updated_number}.xyz"
            print(f"Yeni URL oluşturuluyor: {new_url}")

            # Yeni URL'yi ana_link.txt dosyasına yazıyoruz
            with open("ana_link.txt", "w") as file:
                file.write(new_url)
        else:
            # Yeni URL'yi doğrudan yazıyoruz
            with open("ana_link.txt", "w") as file:
                file.write(current_url)

finally:
    driver.quit()  # Tarayıcıyı kapatıyoruz
