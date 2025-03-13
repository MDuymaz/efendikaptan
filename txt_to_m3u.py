# mac_verileri.txt dosyasını m3u formatına dönüştürme
with open('mac_verileri.txt', 'r', encoding='utf-8') as txt_file:
    content = txt_file.read()  # TXT dosyasının içeriğini oku

with open('mac_verileri.m3u', 'w', encoding='utf-8') as m3u_file:
    m3u_file.write('#EXTM3U\n\n')  # M3U dosyasının başına #EXTM3U ekle
    m3u_file.write(content)  # TXT içeriğini M3U dosyasına yaz

print("M3U dosyası başarıyla oluşturuldu: mac_verileri.m3u")
