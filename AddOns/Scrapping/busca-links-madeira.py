import requests
from bs4 import BeautifulSoup
import csv
import pyodbc

server = 'ilor.database.windows.net'
database = 'casacomvc'
username = 'plorlando@ilor'
password = 'Lulu1509'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

pages = []

sql_insert = """INSERT INTO dbo.base_competitors VALUES (?, ?, ?)"""
site = 'https://www.madeiramadeira.com.br'
pesquisa = 'jolitex'
range_inicial = 0
range_final = 17

for i in range(range_inicial, range_final):
    url = 'https://www.madeiramadeira.com.br/busca?q=' + pesquisa + '&sortby=relevance&resultsperpage=48&page=' + str(i)
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_list = soup.find(class_='container seller__products-box')
    product_list_items = product_list.find_all('a')

    for product in product_list_items:
        link = site+str(product.get('href'))
        print(str(link))
        try:
            values = (site, link, pesquisa)
            cursor.execute(sql_insert, values)
            conn.commit()
        except:
            print("não deu")
