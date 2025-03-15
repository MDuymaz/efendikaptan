from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome sürücüsünü başlat
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Grafik arayüzü olmadan çalışmak için
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL'ye git
url = "https://trgoals1234.xyz/"
driver.get(url)

# HTML içeriğini al
html = driver.page_source

# HTML içeriğini 'base_url.html' dosyasına yaz
with open('base_url.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Sürücüyü kapat
driver.quit()
