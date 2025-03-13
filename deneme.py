from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_redirected_url(shortened_url):
    # WebDriver Manager ile ChromeDriver'ı otomatik indirin
    service = Service(ChromeDriverManager().install())
    
    # Tarayıcıyı başlat
    driver = webdriver.Chrome(service=service)
    
    # Kısaltılmış URL'yi tarayıcıda aç
    driver.get(shortened_url)
    time.sleep(3)  # Sayfanın yüklenmesi için bekle
    current_url = driver.current_url  # Tarayıcının şu anki URL'sini al
    
    # Tarayıcıyı kapat
    driver.quit()

    return current_url

# Kısaltılmış URL
shortened_url = "https://t.ly/gCnNB"
redirected_url = get_redirected_url(shortened_url)

# Yönlendirilmiş URL'yi new_link.txt dosyasına yaz
with open("new_link.txt", "w") as file:
    file.write(redirected_url)

print("Yönlendirilmiş URL, new_link.txt dosyasına yazıldı:", redirected_url)

