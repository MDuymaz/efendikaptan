from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Tarayıcı sürücüsünü başlat
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Hedef web sayfasını aç
    driver.get("https://trgoals1234.xyz/")

    # Sayfanın tam olarak yüklenmesi için bekleyin
    time.sleep(5)

    # Sayfanın HTML içeriğini al
    html_content = driver.page_source

    # Çıktıyı bir dosyaya kaydet
    with open("trgoals1234.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    # Tarayıcıyı kapat
    driver.quit()
    print("HTML içeriği kaydedildi.")
