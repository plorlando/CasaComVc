import requests
import bs4
import pyodbc
############################# NÃO ESTÁ FUNCIONANDO #############################################
server = 'ilor.database.windows.net'
database = 'casacomvc'
username = 'plorlando@ilor'
password = 'Lulu1509'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

pages = []
contador_paginas = 0
contador_itens = 0

sql_insert = """INSERT INTO dbo.produtos_basecompetitors (baseUrl, prodUrl, search) VALUES (?, ?, ?)"""
site = 'http://www.niazi.com.br'
pesquisa = 'sao%20carlos'
range_inicial = 0
range_final = 180

for i in range(range_inicial, range_final):
    url = 'https://www.niazi.com.br/' + str(i) + '?_q=' + str(i) + '&map=ft&page=1'
    pages.append(url)

for item in pages:
    contador_paginas += 1
    page = requests.get(item)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')

    product_list = soup.findAll('section', class_='vtex-product-summary-2-x-container vtex-product-summary-2-x-containerNormal overflow-hidden br3 h-100 w-100 flex flex-column justify-between center tc')
    print(len(product_list))
    product_list_items = product_list.find_all('a')

    for product in product_list:
        contador_itens += 1
        link = product.get('href')
        try:
            print(str(contador_itens) + " - " + link)
            values = (site, link, pesquisa)
            # cursor.execute(sql_insert, values)
            # conn.commit()
        except:
            print("não deu")

    print('Página: ' + str(contador_paginas))

conn.close()

