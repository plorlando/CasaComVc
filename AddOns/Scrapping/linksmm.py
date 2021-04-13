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

sql_insert = """INSERT INTO dbo.produtos_basecompetitors (baseUrl, prodUrl, search) VALUES (?, ?, ?)"""
site = 'https://www.madeiramadeira.com.br'
pesquisa = 'corttex'
range_inicial = 0
range_final = 15

for i in range(range_inicial, range_final):
    url = 'https://www.madeiramadeira.com.br/busca?q=' + pesquisa + '&sortby=relevance&resultsperpage=48&page=' + str(i)
    pages.append(url)

contadorDePagina = 0
contadoDeLinksTotal = 0

##############################################################

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    # product_list = soup.find('div', class_='product__name')
    product_list_items = soup.find_all('a')

    contadorDeLinks = 1

    for product in product_list_items:
        link = site+str(product.get('href'))

        try:
            values = (site, link, pesquisa)
            cursor.execute(sql_insert, values)
            conn.commit()
            print(str(link))
        except:
            print("não deu")

        contadorDeLinks += 1
        contadoDeLinksTotal += 1

    print("PÁGINA: " + str(contadorDePagina))
    contadorDePagina += 1