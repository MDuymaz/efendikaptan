from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Headless modda çalıştır
options.add_argument("--no-sandbox")  # Güvenlik sandviçini devre dışı bırak
options.add_argument("--disable-dev-shm-usage")  # Bellek paylaşımı sorunlarını önlemek için

# WebDriver'ı başlatın
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Web sitesinin URL'sini belirtin
url = "https://trgoals1234.xyz/"

# Sayfayı yükle
driver.get(url)

# Sayfanın tamamen yüklenmesini beklemek için bir süre bekleyin
time.sleep(5)  # Sayfanın yüklenmesi için 5 saniye bekleyelim

# Tüm <script> etiketlerini bul
scripts = driver.find_elements(By.TAG_NAME, 'script')

# HTML içeriğini kaydedeceğimiz dosyayı aç
with open("scripts_output_selenium.html", "w", encoding="utf-8") as file:
    # HTML dosyasının başını yaz
    file.write("<html><head><title>Script İçerikleri</title></head><body>\n")
    file.write("<h1>Web Sayfasındaki Script Etiketleri</h1>\n")
    
    # Her bir <script> etiketinin içeriğini dosyaya yaz
    for i, script in enumerate(scripts):
        script_content = script.get_attribute('innerHTML')  # script içeriğini al
        if script_content:
            file.write(f"<h2>Script #{i+1}</h2>\n")
            file.write(f"<pre>{script_content}</pre>\n")
    
    # HTML dosyasının sonunu yaz
    file.write("</body></html>\n")

# Tarayıcıyı kapat
driver.quit()

print("Script içerikleri başarıyla kaydedildi: scripts_output_selenium.html")
