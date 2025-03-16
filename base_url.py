from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# ana_link.txt dosyasından URL'yi oku
with open('ana_link.txt', 'r') as file:
    base_url = file.read().strip()  # URL'yi dosyadan al ve boşluklardan temizle

# URL'yi oluştur
url = f"{base_url}/channel.html?id=yayin1"

# Chrome seçeneklerini ayarla
chrome_options = Options()
chrome_options.add_argument("--headless")  # Başsız (headless) modda çalıştırmak için
chrome_options.add_argument("--no-sandbox")  # Sandbox kullanmamak
chrome_options.add_argument("--disable-dev-shm-usage")  # /dev/shm kullanımını engelle

# Tarayıcıyı başlatmak için gerekli path ve driver'ı ayarla
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Sayfayı aç
driver.get(url)

# Sayfanın tamamen yüklenmesi için bir süre bekle
time.sleep(5)

# JavaScript ile tanımlanmış olan baseurl değişkenini almak
baseurl = driver.execute_script("return baseurl;")

# baseurl'i yazdır
print("Base URL:", baseurl)

# base_url.txt dosyasının yolunu tanımla
base_url_file_path = 'base_url.txt'

# Dosya var mı kontrol et
if not os.path.exists(base_url_file_path):
    print(f"{base_url_file_path} dosyası bulunamadı, yeni dosya oluşturulacak.")
else:
    print(f"{base_url_file_path} dosyası bulundu.")

# baseurl'i base_url.txt dosyasına yaz
try:
    with open(base_url_file_path, 'w', encoding='utf-8') as file:
        file.write(baseurl)
    print(f"Base URL dosyaya başarıyla yazıldı: {baseurl}")
except Exception as e:
    print(f"Dosyaya yazma hatası: {e}")

# Yazdıktan sonra dosyayı tekrar oku ve kontrol et
with open(base_url_file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()
    print(f"Dosya içeriği: {file_content}")

# Tarayıcıyı kapat
driver.quit()
