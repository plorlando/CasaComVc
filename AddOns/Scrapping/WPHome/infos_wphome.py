import datetime as datetime
import lxml.html as parser
import requests
import pyodbc
import datetime
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

server = 'ilor.database.windows.net'
database = 'casacomvc'
username = 'plorlando@ilor'
password = 'Lulu1509'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

sql = "SELECT prod_url, casa_ean FROM dbo.produtos_basecompetitors where base_url like '%wphome%'"
cursor.execute(sql)
result = cursor.fetchall()

product_desc = "//h1/text()"
product_code = "//strong[@id='product-reference']/text()"
product_price = "//span[@id='variacaoPreco']/text()"
base_url = 'https://www.wphome.com.br/'

sql_insert = """INSERT INTO dbo.produtos_pricehistory (data, base_url, prod_url, product_desc, site_prod_code, prod_price, casa_ean) VALUES (?, ?, ?, ?, ?, ?, ?)"""

contador_itens = 0
contador_sucesso = 0
contador_falha = 0
wphometxt = open('wphome.csv', 'a')

try:
    for i in result:
        contador_itens += 1
        product_url = i[0]
        ean = i[1]
        try:
            html = urlopen(product_url)
            r = requests.get(product_url)
            html = parser.fromstring(r.text)

            prod = html.xpath(product_desc)
            produto = str(prod).replace('['', '').replace('']', '').replace('[', '.').replace(']', '.').replace('..', '')

            cod = html.xpath(product_code)
            codigo = str(cod).replace('['', '').replace('']', '').replace('[', '.').replace(']', '.').replace('..', '')

            p = html.xpath(product_price)
            preco = float(str(p).replace('['', '').replace('']', '').replace('R$ ', '').replace('.', '').replace(',', '.').replace('[', '.').replace(']', '.').replace('..', '').replace(".'", '').replace("'.", '').replace(" ", ''))

            data_atualiz = datetime.datetime.now()

            values = (data_atualiz, base_url, product_url, produto, codigo, preco, ean)
            # cursor.execute(sql_insert, values)
            # conn.commit()
            print(str(contador_itens) + ', ' + product_url + ', ' + str(preco) + ', ' + str(data_atualiz))
            contador_sucesso += 1

        except HTTPError as e:
            contador_falha += 1
            print(str(contador_itens) + ', ' + 'ERRO: ' + product_url + ', ' + str(e))
            wphometxt.writelines(str(contador_itens) + ', ' + product_url + ', ' + str(e) + ', ' + str(data_atualiz) + '\n')
        except URLError as e1:
            contador_falha += 1
            print(str(contador_itens) + ', ' + 'ERRO: ' + product_url + ', Server down or incorrect domain')
            wphometxt.writelines(str(contador_itens) + ', ' + product_url + ', ' + str(e1) + ', ' + str(data_atualiz) + '\n')
        except ValueError as e2:
            contador_falha += 1
            print(str(contador_itens) + ', ' + 'ERRO: ' + product_url + ', Erro no valor do produto, ' + str(e2))
            wphometxt.writelines(str(contador_itens) + ', ' + product_url + ', ' + str(e2) + ', ' + str(data_atualiz) + '\n')
finally:
    print('Itens bem sucedidos: ' + str(contador_sucesso))
    print('Itens mal sucedidos: ' + str(contador_falha))
    print('Itens processados: ' + str(contador_itens))
    conn.close()

