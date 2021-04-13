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
contador_paginas = 0
contador_itens = 0

sql_insert = """INSERT INTO dbo.produtos_basecompetitors (base_url, prod_url, search) VALUES (?, ?, ?)"""
site = 'https://www.wphome.com.br/'
pesquisa = 'kacyumara'
range_inicial = 0
range_final = 1
classe = 'showcase-catalog clearfix col-sm-12 col-md-12'

for i in range(range_inicial, range_final):
    url = 'https://www.wphome.com.br/loja/busca.php?loja=608097&palavra_busca=' + pesquisa + '&pg=' + str(i)
    pages.append(url)

for item in pages:
    contador_paginas += 1
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_list = soup.find(class_=classe)
    product_list_items = product_list.find_all('a')

    for product in product_list_items:
        contador_itens += 1
        link = product.get('href')
        try:
            print(str(contador_itens) + " - " + link)
            # values = (site, link, pesquisa)
            # cursor.execute(sql_insert, values)
            # conn.commit()
        except:
            print("não deu")

    print('Página: ' + str(contador_paginas))

conn.close()