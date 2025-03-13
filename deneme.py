import requests
from bs4 import BeautifulSoup

# URL'yi al
url = "https://bit.ly/m/taraftarium24w"
response = requests.get(url)

# Sayfanın içeriğini çöz
soup = BeautifulSoup(response.content, 'html.parser')

# İlk linki bul
first_link = soup.select_one("section.links a")["href"]

# Kısaltılmış linkin çözülmesi
redirect_response = requests.head(first_link, allow_redirects=True)
final_link = redirect_response.url

# Linki dosyaya yaz
with open('yeni_link.txt', 'w') as file:
    file.write(final_link)
