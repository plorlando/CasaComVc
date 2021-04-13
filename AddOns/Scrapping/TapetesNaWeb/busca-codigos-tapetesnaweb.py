import requests
from bs4 import BeautifulSoup
import csv
import pyodbc
import json

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
site = 'http://www.tapetesnaweb.com.br'
pesquisa = 'abdalla'
range_inicial = 1
range_final = 2

for i in range(range_inicial, range_final):
    url = 'https://www.tapetesnaweb.com.br/resultadopesquisa?pag=' + str(i) + '&departamento=&buscarpor='+ pesquisa +'&smart=0'
    pages.append(url)

for item in pages:
    contador_paginas += 1
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_list = soup.find_all(class_='collection-productName')

    for x in product_list:
        contador_itens += 1
        text = x['href']
        text2 = text.split('window.location=')
        link = text2[1].replace("'", '').replace(';', '')
        try:
            print(str(contador_itens) + " - " + link)
            # values = (site, link, pesquisa)
            # cursor.execute(sql_insert, values)
            # conn.commit()
        except:
            print("não deu")

    print('Página: ' + str(contador_paginas))




