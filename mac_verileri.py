import requests
from bs4 import BeautifulSoup

# base_url.txt dosyasından URL'yi oku
with open('base_url.txt', 'r') as file:
    base_url = file.read().strip()  # base_url'i dosyadan al ve boşluklardan temizle

# ana_link.txt dosyasından URL'yi oku
with open('ana_link.txt', 'r') as file:
    url = file.read().strip()  # URL'yi dosyadan al ve boşluklardan temizle

# Web sayfasını alma
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
            
            # Yeni URL'i base_url.txt'den okunan URL ile oluşturma
            yeni_url = f"{base_url}{data_url}.m3u8"
            
            # Sabit metni verinin üstüne ekleme
            sabit_metin = f"#EXTVLCOPT:http-user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)\n#EXTVLCOPT:http-referrer={url}\n"
            # Saatte "CANLI" varsa "CANLI" olarak group-title değeri, yoksa "MAÇLAR"
            group_title = "CANLI" if "CANLI" in saat else "MAÇLAR"
            # EXTINF satırı
            extinf = f"#EXTINF:-1 tvg-name=\"{takimlar}\" tvg-language=\"Turkish\" tvg-country=\"TR\" tvg-id=\"Spor_{takimlar.replace(' ', '')}\" tvg-logo=\"https://e7.pngegg.com/pngimages/955/749/png-clipart-ape-monkey-cartoon-sad-monkey-face-mammal-vertebrate.png\" group-title=\"{group_title}\",{saat} {takimlar}"
            # Veriyi formatla
            veri = f"{extinf}\n{sabit_metin}{yeni_url}"
            veriler.append(veri)
        
        # Verileri bir metin dosyasına kaydetme
        with open('mac_verileri.txt', 'w', encoding='utf-8') as file:
            for veri in veriler:
                file.write(veri + "\n\n")  # Her veri arasında boş satır bırak
            
        print("Veriler başarıyla kaydedildi: mac_verileri.txt")
    else:
        print("Belirtilen div bulunamadı.")
else:
    print("İstek başarısız oldu:", response.status_code)
