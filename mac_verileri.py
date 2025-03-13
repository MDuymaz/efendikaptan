import requests
from bs4 import BeautifulSoup
import time

# Siteyi kontrol etme fonksiyonu
def check_site_name():
    url = "https://trgoals1226.xyz/"
    
    # Web sayfasını alma
    response = requests.get(url)

    # Sayfanın durumunu kontrol et
    if response.status_code == 200:
        # Sayfanın içeriğini çözümleme
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Sayfa başlığını alalım (veya başka bir site ismi elde etme yöntemine göre değiştirebilirsiniz)
        site_title = soup.title.text.strip()
        
        return site_title
    else:
        print("İstek başarısız oldu:", response.status_code)
        return None

# mac_verileri.py dosyasındaki site URL'sini güncelleme fonksiyonu
def update_site_in_code(new_site_name):
    with open("mac_verileri.py", "r", encoding="utf-8") as file:
        code = file.read()

    # Eski URL'yi bul ve yeni URL ile değiştir
    old_url = "https://trgoals1226.xyz/"
    new_url = f"https://{new_site_name}/"
    
    if old_url in code:
        code = code.replace(old_url, new_url)
        print(f"URL güncellendi: {old_url} => {new_url}")
        
        # Sabit metni güncelleme
        old_referrer = "http-referrer=https://trgoals1225.xyz/"
        new_referrer = f"http-referrer=https://{new_site_name}/"
        
        if old_referrer in code:
            code = code.replace(old_referrer, new_referrer)
            print(f"Referrer güncellendi: {old_referrer} => {new_referrer}")
        
        # Dosyayı güncel içerik ile yazma
        with open("mac_verileri.py", "w", encoding="utf-8") as file:
            file.write(code)
        print("mac_verileri.py dosyası başarıyla güncellendi.")
    else:
        print("Eski URL dosyada bulunamadı.")

# Site adı değişti mi kontrol etme
def check_and_update_if_needed():
    # Önce mevcut siteyi kontrol et
    current_site_name = check_site_name()
    
    if current_site_name:
        # Yeni site adını kaydetmek ve dosyayı güncellemek
        if current_site_name != "trgoals1226.xyz":
            update_site_in_code(current_site_name)
        else:
            print("Site adı değişmedi.")
    else:
        print("Site adı alınamadı, işlem yapılamadı.")

# Hedef URL
url = "https://trgoals1226.xyz/"

# Web sayfasını alma
def fetch_data():
    response = requests.get(url)

    # Sayfanın durumunu kontrol et
    if response.status_code == 200:
        # Sayfanın içeriğini çözümleme
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Belirtilen div'i bulma
        mac_liste_div = soup.find('div', class_='macListeWrapper')

        # Verileri kaydetmek için bir liste
        veriler = []
        
        # Eğer div bulunduysa, içindeki her bir "mac" div'ini döngüye al
        if mac_liste_div:
            mac_divler = mac_liste_div.find_all('div', class_='mac')
            for mac in mac_divler:
                saat = mac.find('span', class_='saat').text.strip()
                takimlar = mac.find('span', class_='takimlar').text.strip()
                data_url = mac['data-url'].replace("/channel.html?id=", "")  # 'id=' kısımlarını kaldır
                
                # Yeni URL'i ekleme
                yeni_url = f"https://o0.b4c8d3e9f1a2b7c5d85.cfd/{data_url}.m3u8"
                
                 # Sabit metni verinin üstüne ekleme
                sabit_metin = f"#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)\n#EXTVLCOPT:http-referrer=https://{url.split('/')[2]}/\n"
                # EXTINF satırı
                extinf = f"#EXTINF:-1 tvg-name=\"beIN SPORTS 1\" tvg-language=\"Turkish\" tvg-country=\"TR\" tvg-id=\"Spor_beINSPORTS\" tvg-logo=\"https://e7.pngegg.com/pngimages/955/749/png-clipart-ape-monkey-cartoon-sad-monkey-face-mammal-vertebrate.png\" group-title=\"TRGoals\",{saat} {takimlar}"
                # Veriyi formatla
                veri = f"{extinf}\n{sabit_metin}{yeni_url}"
                veriler.append(veri)
            
            # Verileri bir metin dosyasına kaydetme
            with open('mac_verileri.txt', 'w', encoding='utf-8') as file:
                for veri in veriler:
                    file.write(veri + "\n\n")  # Her veri arasında boş satır bırak
                
            print("Veriler başarıyla kaydedildi: mac_verileri.txt")

            # Site adı kontrolü ve güncellemesi
            check_and_update_if_needed()

        else:
            print("Belirtilen div bulunamadı.")
    else:
        print("İstek başarısız oldu:", response.status_code)
