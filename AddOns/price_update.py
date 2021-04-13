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
book = xlrd.open_workbook('d:/OneDrive/CasaComVc/Modelos/price_update.xlsx')
sheet = book.sheet_by_name('Planilha1')
print('Sheet by names: ', book.sheet_names())

query = """UPDATE dbo.produtos_produtos
           SET custo_base = ?
           WHERE id = ?"""

# grab existing row count in the database for validation later
cursor.execute("SELECT count(*) FROM dbo.produtos_produtos")
before_import = cursor.fetchone()

contador = 1

for row in range(1, sheet.nrows):
    id = sheet.cell(row, 0).value
    price = sheet.cell(row, 5).value

    # Assign values from each row
    values = (price, id)

    # Execute sql Query
    cursor.execute(query, values)
    print(str(contador) + " " + "ID: " + str(id) + " - PREÇO: " + str(price))
    contador += 1

    # Commit the transaction
    conn.commit()

# If you want to check if all rows are imported
cursor.execute("SELECT count(*) FROM dbo.produtos_produtos")
result = cursor.fetchone()

print((result[0] - before_import[0]))  # should be True

# Close the database connection
conn.close()