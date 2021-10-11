import requests
from bs4 import BeautifulSoup
import time

lapakrumah = []

for pages in range(1,8):
    url = 'https://www.rumahku.com/dijual/tanah/page:'

    headers = {'user agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
               }

    respons = requests.get(url+str(pages), headers=headers)
    # print(respons)
    soup = BeautifulSoup(respons.text, 'html.parser')
    content = soup.findAll('div', class_='col-md-6 grid-item')
    # print(content)
    for item in content:
        name = item.find('h3').text.strip()
        try:
            address = item.find('p').text.strip()
        except:
            address = ('Tidak ada alamat')
        price = item.find('h5').text.strip()

        info_property = {
            "name": name,
            "address": address,
            "price": price
        }
        lapakrumah.append(info_property)
    print(len(lapakrumah))
    time.sleep(0)

print(lapakrumah)