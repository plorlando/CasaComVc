# IMPORTA OS PRODUTOS PARA A BASE ATUAL
import pyodbc
import xlrd

date_format = '%d/%m/%Y'

# create Connection and Cursor objects
server = 'ilor.database.windows.net'
database = 'casacomvc'
username = 'plorlando@ilor'
password = 'Lulu1509'
driver = '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = conn.cursor()

# Open the workbook and define the worksheet
book = xlrd.open_workbook('d:/OneDrive/CasaComVc/Modelos/hpt.xlsx')
sheet = book.sheet_by_name('Planilha1')
print('Sheet by names: ', book.sheet_names())

query = """UPDATE dbo.produtos_produtos
           SET custo_base = ?
           WHERE ean_prod = ? AND id_forn = 'HPT'"""

contador = 1

for row in range(1, sheet.nrows):
    ean_prod = sheet.cell(row, 7).value
    price = round(sheet.cell(row, 4).value, 2)

    # Assign values from each row
    values = (price, ean_prod)

    # Execute sql Query
    cursor.execute(query, values)
    print(str(contador) + " " + "ID: " + str(ean_prod) + " - PREÇO: " + str(price))
    contador += 1

    # Commit the transaction
    conn.commit()

print('Total de atualizações: ' + str(contador))  # should be True

# Close the database connection
conn.close()