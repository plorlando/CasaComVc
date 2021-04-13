import requests
from bs4 import BeautifulSoup
import csv
import pyodbc

server = 'ilor.database.windows.net'
database = 'casacomvc'
username = 'plorlando@ilor'
password = 'Lulu1509'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

pages = []

sql_insert = """INSERT INTO dbo.price_history VALUES (?, ?, ?, ?, ?, ?)"""

for i in range(0, 85):
    url = 'https://www.tapetesnaweb.com.br/resultadopesquisa?pag='+str(i)+'&departamento=&buscarpor=s%c3%a3o+carlos&smart=0'
    pages.append(url)

with open('links.csv', mode='w', newline='') as csvfile:
    linkwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    linkwriter.writerow(['site', 'pesquisa', 'link'])
    site = 'http://www.tapetesnaweb.com.br'
    pesquisa = 'sao carlos'

    for item in pages:
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'html.parser')

        product_list = soup.find(class_='vitrine_dept')
        product_list_items = product_list.find_all('a')

        for product in product_list_items:
            link = product.get('href')
            print(link)
            # print(product.prettify())

            linkwriter.writerow([site, pesquisa, link])

