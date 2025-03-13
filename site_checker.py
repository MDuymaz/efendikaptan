import requests
from bs4 import BeautifulSoup
import os

# Önceki site ismini bir dosyadan okuma
def get_previous_site_name():
    try:
        with open("previous_site_name.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

# Yeni site ismini kontrol etme
def get_current_site_name():
    url = "https://trgoals1226.xyz/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Site adını başlık (title) etiketinden alalım
        site_name = soup.title.text.strip()
        return site_name
    else:
        print("Siteye ulaşılamadı.")
        return None

# Yeni site ismini kaydetme
def save_site_name(site_name):
    with open("previous_site_name.txt", "w") as file:
        file.write(site_name)

# Ana kontrol fonksiyonu
def check_site_name_change():
    previous_site_name = get_previous_site_name()
    current_site_name = get_current_site_name()

    if previous_site_name and current_site_name:
        if previous_site_name != current_site_name:
            print(f"Site adı değişti! Önceki: {previous_site_name}, Yeni: {current_site_name}")
            save_site_name(current_site_name)
        else:
            print("Site adı değişmedi.")
    elif not previous_site_name:
        print("İlk kontrol: Site adı kaydedildi.")
        save_site_name(current_site_name)

if __name__ == "__main__":
    check_site_name_change()
