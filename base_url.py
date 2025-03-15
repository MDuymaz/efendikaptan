import requests
from bs4 import BeautifulSoup

# ana_link.txt dosyasından URL'yi okuyoruz
with open('ana_link.txt', 'r') as file:
    url = file.read().strip()  # URL'yi okuyoruz ve varsa boşlukları kaldırıyoruz

# Web sayfasını GET isteği ile alıyoruz
response = requests.get(url)

# Eğer isteğimiz başarılı olduysa, HTML içeriğini işleme alıyoruz
if response.status_code == 200:
    # HTML içeriğini BeautifulSoup ile analiz ediyoruz
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 'mainContainer' sınıfına sahip olan section'ı buluyoruz
    main_container = soup.find('section', class_='mainContainer')
    
    # Eğer base tag'ı varsa, href özniteliğini alıyoruz
    base_tag = soup.find('base')
    if base_tag and base_tag.get('href'):
        base_url = base_tag.get('href')
        
        # Base URL'yi bir txt dosyasına yazıyoruz
        with open('baseurl.txt', 'w') as file:
            file.write(base_url)
        
        print("Base URL başarıyla baseurl.txt dosyasına yazıldı.")
    else:
        print("Base URL bulunamadı.")
else:
    print("Web sitesine bağlanırken bir hata oluştu. Status code:", response.status_code)
