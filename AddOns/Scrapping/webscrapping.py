import lxml.html as parser
import requests
import csv
from urllib.parse import urlsplit, urljoin
import xlrd

file = xlrd.open_workbook("D:/Documents/Scrapping/database.xlsx")
df = file.sheet_by_index(0)

product = "//span[@id='lblNome']/text()"
price = "//p[@itemprop='price']/text()"
print(df.nrows)

for r in range(1, df.nrows):
    product_url = df.cell(r, 2).value
    produto = df.cell(r, 3).value
    r = requests.get(product_url)
    html = parser.fromstring(r.text)
    prod = html.xpath(produto)
    preco = html.xpath(price)
    print(prod)
    print(preco)

