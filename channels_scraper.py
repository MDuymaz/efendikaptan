import requests
from bs4 import BeautifulSoup
import time

def fetch_channels(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    channels = []
    
    # 'macListe' div'ini seçin
    mac_liste = soup.find('div', id='hepsi')
    
    # 'takimlar' ve 'data-url' içeriğini alın
    takimlar = mac_liste.find_all('span', class_='takimlar')
    
    for takim in takimlar:
        channel_name = takim.get_text(strip=True)

        # 'data-url' değerini almak için üst öğeyi bulun
        parent = takim.find_parent()
        if parent and 'data-url' in parent.attrs:
            channel_link = parent['data-url']
        else:
            channel_link = None
        
        channels.append((channel_name, channel_link))
        
    return channels

def save_to_m3u(channels, filename='channels.m3u'):
    with open(filename, 'w') as f:
        f.write('#EXTM3U\n')
        for name, link in channels:
            f.write(f'#EXTINF:-1,{name}\n')
            f.write(f'{link}\n')

def main(url, interval=60):
    while True:
        print("Fetching channels...")
        channels = fetch_channels(url)
        save_to_m3u(channels)
        print(f"Saved {len(channels)} channels to M3U file.")
        time.sleep(interval)

if __name__ == '__main__':
    URL = 'https://trgoals1226.xyz/'  # Belirtilen sitenin URL'si.
    INTERVAL = 3600  # Kontrol aralığı (saniye cinsinden), burada 3600 saniye (1 saat) olarak ayarlanmıştır.
    
    main(URL, INTERVAL)
