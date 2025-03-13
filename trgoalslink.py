import requests
from bs4 import BeautifulSoup

# URL'yi tanımla
url = 'https://trgoalsgiris.xyz'
response = requests.get(url)

# HTML'i parse et
soup = BeautifulSoup(response.text, 'html.parser')

# İlk 'buttons' div'inin içindeki ilk linki al
first_link = soup.find('div', class_='buttons').find('a').get('href')

# Bağlantıyı dosyaya yaz
with open('link.txt', 'w') as file:
    file.write(first_link)
