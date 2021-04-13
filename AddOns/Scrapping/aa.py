import functions
import pyodbc
import time

inicio = time.time()

server = 'ilor.database.windows.net'
database = 'casacomvc'
username = 'plorlando@ilor'
password = 'Lulu1509'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

sql_insert = """INSERT INTO dbo.produtos_pricehistory (data, prodUrl, productDesc, siteProdCode, prodPrice, baseUrl, casaEan) VALUES (?, ?, ?, ?, ?, ?, ?)"""

functions.LojasDonna(cursor, conn, sql_insert)

conn.close()

fim = time.time()
print("FIM: " + str((fim - inicio) / 60) + " minutos.")

