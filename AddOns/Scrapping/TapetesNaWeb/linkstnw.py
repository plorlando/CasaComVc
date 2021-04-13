import requests
import pyodbc
from bs4 import BeautifulSoup

server = 'ilor.database.windows.net'
database = 'casacomvc'
username = 'plorlando@ilor'
password = 'Lulu1509'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

urls = []

sql_insert = """INSERT INTO dbo.produtos_basecompetitors (baseUrl, prodUrl, search) VALUES (?, ?, ?)"""
site = 'https://www.tapetesnaweb.com.br'
pesquisa = 'kapazi'
range_inicial = 0
range_final = 10

for i in range(range_inicial, range_final):
    url = 'https://www.tapetesnaweb.com.br/resultadopesquisa?pag=' + str(i) + '&departamento=&buscarpor='+ pesquisa +'&smart=0'
    urls.append(url)

contadorDePagina = 0
contadoDeLinksTotal = 1

##############################################################

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tabela = soup.findAll('h3', class_='titulodept')
    print(tabela)

    contadorDeLinks = 1

    for i in tabela:
        a = str(i).split('window.location=')
        b = str(a[1]).split(';')
        c = b[0].replace("'", '')

        try:
            values = (site, c, pesquisa)
            cursor.execute(sql_insert, values)
            conn.commit()
            print("Link No: " + str(contadorDeLinks) + "/" + str(contadoDeLinksTotal) + " - " + c)
        except:
            print("commit NÃO ok")

        contadorDeLinks += 1
        contadoDeLinksTotal += 1

    print("PÁGINA: " + str(contadorDePagina))
    contadorDePagina += 1


##############################################################

print("TOTAL DE LINKS: " + str(contadoDeLinksTotal))
print("PROCESSAMENTO FINALIZADO")

conn.close()