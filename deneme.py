from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver'ı başlatıyoruz
options = Options()
options.add_argument('--headless')  # Tarayıcıyı gizli (headless) modda çalıştırıyoruz.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Verilen URL'yi açıyoruz
    driver.get("https://bit.ly/m/taraftarium24w")
    
    # Sayfanın tam olarak yüklenmesi için bir süre bekliyoruz
    time.sleep(5)  # Sayfanın yüklenmesini beklemek için kullanılabilir.
    
    # XPath ile butona tıklıyoruz
    button = driver.find_element(By.XPATH, "/html/body/div/div/div/main/section[1]/a[1]")
    button.click()

    # Sayfanın URL'sini alıyoruz (veya istediğiniz başka bir bilgiyi)
    current_url = driver.current_url  # Tıklanan sayfanın URL'sini alıyoruz.
    
    # Çıkan sonucu dosyaya yazdırıyoruz
    with open("ana.link.txt", "w") as file:
        file.write(current_url)  # Burada URL'yi yazdırıyoruz. Farklı bir veri yazabilirsiniz.

    print(f"Sonuç kaydedildi: {current_url}")

finally:
    # Tarayıcıyı kapatıyoruz
    driver.quit()
