import requests
from bs4 import BeautifulSoup
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
site = 'https://www.lojasdonna.com.br/'
pesquisa = 'kapazi'
range_inicial = 0
range_final = 10

for i in range(range_inicial, range_final):
    url = 'https://www.lojasdonna.com.br/resultadopesquisa?pag=' + str(i) + '&departamento=&buscarpor='+ pesquisa +'&smart=0'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_list = soup.find(class_='vitrine_geral')
    product_list_items = product_list.find_all('a')

    for product in product_list_items:
        link = product.get('href')
        try:
            values = (site, link, pesquisa)
            cursor.execute(sql_insert, values)
            conn.commit()
            print(link)
        except:
            print("não deu")
