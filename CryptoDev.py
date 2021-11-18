import requests

#Приветствие программы
print('''Вас приветствует CryproDev \n Внимание! Это лишь бета версия приложения, ждите обновления''')
name = input("Введите своё имя: ")

#Меню вывода
print("Здравствуйте, " + name + ". сделайте выбор в меню.")
print('''\n\n 1.Курсы валют \n 2.Прогнозы \n 3.Покупка валюты \n 4.Новая криптовалюта \n 5.Настройки \n 6.Выйти \n\n''')

#Блок вывода курса Bitcoin
def scrape():
response = requests.get(URL)
response_json = response.json()
return float(response_json["USD"]["last"])
URL = 'https://blockchain.info/ru/ticker'
last_price = None
while True:
latest_price = scrape()
if latest_price != last_price:
print("Последняя цена BTC: ", latest_price)
last_price = latest_price
