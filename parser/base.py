import requests
from bs4 import BeautifulSoup as BS
from db import get_cars
from pprint import pprint as pp

URL = "https://cars.kg/offers"
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
           "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"}


url = URL
response = requests.get(url, headers=headers)
print(response.status_code)


def remove_extra_spaces(text: str) -> str:
    return ' '.join(text.replace('\n', '').split())


soup = BS(response.text, "html.parser")
table = soup.find('div', class_="catalog-list")
cars = []
for item in table.findAll('a', class_="catalog-list-item"):
    model = remove_extra_spaces(item.find(class_="catalog-item-params").text)
    price = remove_extra_spaces(item.find('span', class_="catalog-item-price").text)
    mileage = remove_extra_spaces(item.find('span', class_="catalog-item-mileage").text)
    info = remove_extra_spaces(item.find('span', class_="catalog-item-descr").text)
    cars.append((model, price, mileage, info))
get_cars(cars)
pp(cars)



# classwork
# import requests
# from bs4 import BeautifulSoup as BS
# from pprint import pp
#
#
# URL = 'https://mashina.kg'
# response = requests.get(URL)
# # print(response.status_code)
# # print(response)
# # pp(response)
# # pp(dir(response))
# #
# # print(response.text[:200])
#
# soup = BS(response.text, "html.parser")
# table = soup.find('div', class_="category-block-content")
# cars = []
# for obyava in table.findAll('a'):
#     car = {}
#     car['name'] = obyava.find('h2'.class_="name")
#     car['price'] = obyava.find('div', class_="block price").find('strong')
#
#     cars.append(car)
#     print(cars)
#
#     # print(obyava.text.strip().replace(' ',''))