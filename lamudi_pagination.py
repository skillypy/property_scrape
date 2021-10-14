import requests
from bs4 import BeautifulSoup
import time

forsale = []
count = 0

for pages in range(1,4):
    url = 'https://www.lamudi.co.id/land/buy/?page='

    headers = {'user agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
               }

    respons = requests.get(url+str(pages), headers=headers)
    soup = BeautifulSoup(respons.text, 'lxml')
    content = soup.findAll('div', class_='row ListingCell-row ListingCell-agent-redesign')
    # img = soup.findAll('img')
    for item in content:
        name = item.find('h2').text.strip()
        address = item.find('span', class_='ListingCell-KeyInfo-address-text').text.strip()
        try:
            price = item.find('span', class_='PriceSection-FirstPrice').text.strip()
        except:
            price = 'Kontak agen untuk harga'
        meters = item.find('div', class_='KeyInformation-description_v2').find('span').text.strip()
        pic = item.find('img')['data-src']

        info_property = {
            "name": name,
            "address": address,
            "price": price,
            "meters": meters,
            "picture": pic
        }

        forsale.append(info_property)
    count += 1
    print(f"Halaman ke -",count,",item yang di scrape :",len(forsale))
    time.sleep(1)

print('Hasilnya sebagai berikut :\n',forsale)