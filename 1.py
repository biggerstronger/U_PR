import requests
import csv
from bs4 import BeautifulSoup as bs
import os


def get_data(url):
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    name = [element.text for element in soup.find('tbody').find_all(class_='cmc-table__cell--sort-by__name')]
    price = [element.text for element in soup.find('tbody').find_all(class_='cmc-table__cell--sort-by__market-cap')]
    market_cap = [element.text for element in soup.find('tbody').find_all(class_='cmc-table__cell--sort-by__price')]
    for i in range(len(name)):
        Table = {'Name': name[i],
                 'Market_cap': market_cap[i],
                 'Price': price[i]}
        try:
            with open('data.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow((Table['Name'],
                                 Table['Market_cap'],
                                 Table['Price']))
        except IOError:
            open('data.csv', 'wb')
    file.close()


def search_name():
    with open('data.csv', "r") as file:
        search = input('Введите название криптовалюты: ')
        fileReader = csv.reader(file)
        for row in fileReader:
            for field in row:
                if field == search:
                    print(row)
                    break


def main():
    try:
        os.system(r' >data.csv')
    except:
        os.system(r'nul>data.csv')
    url = 'https://coinmarketcap.com/'
    get_data(url)
    search_name()


if __name__ == '__main__':
    main()
