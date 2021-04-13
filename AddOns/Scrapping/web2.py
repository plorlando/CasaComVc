import lxml.html as parser
import requests
import pyodbc
import datetime
import csv
from urllib.parse import urlsplit, urljoin
import xlrd

server = 'ilor.database.windows.net'
database = 'casacomvc'
username = 'plorlando@ilor'
password = 'Lulu1509'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

sql = "SELECT product_url FROM dbo.base_competitors"
cursor.execute(sql)
result = cursor.fetchall()

tnw_product_desc = "//span[@id='lblNome']/text()"
tnw_product_code = "//span[@id='lblCodigoProduto']/text()"
tnw_product_price = "//p[@itemprop='price']/text()"
tnw_base_url = "www.tapetesnaweb.com.br"

sql_insert = """INSERT INTO dbo.price_history VALUES (?, ?, ?, ?, ?, ?)"""

try:
    for i in result:
        product_url = i[0]
        r = requests.get(product_url)
        html = parser.fromstring(r.text)
        prod = html.xpath(tnw_product_desc)
        produto = str(prod).replace("['", "").replace("']", "")
        cod = html.xpath(tnw_product_code)
        codigo = str(cod).replace("['", "").replace("']", "")
        p = html.xpath(tnw_product_price)
        preco = float(str(p).replace("['", "").replace("']", "").replace("R$ ", "").replace(".","").replace(",", "."))
        data_atualiz = datetime.datetime.now()

        values = (data_atualiz, str(product_url), produto, codigo, preco, str(tnw_base_url))
        cursor.execute(sql_insert, values)
        conn.commit()

        print(produto)
        print(codigo)
        print(preco)
        print(data_atualiz)
        print(tnw_base_url)
        print(product_url)
        print("------")
finally:
    conn.close()

