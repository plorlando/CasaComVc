# Importar bibliotecas
from datetime import date
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
book = xlrd.open_workbook('d:/OneDrive/CasaComVc/Cadastro/estoque sao carlos.xlsx')
sheet = book.sheet_by_name('Sheet1')
print('Sheet by names: ', book.sheet_names())

query = """INSERT INTO dbo.produtos_produtos (ean_prod, id_cat_sub, familia_forn, cor, complemento, sub_familia_forn,
    un_venda, prod_med, qtde_estoque_forn, custo_base, cod_fam_forn, ncm, id_forn, desconto, mkp1, mkp2, mkp3,
    data_cadastro, produto, desc_tray)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

# grab existing row count in the database for validation later
cursor.execute("SELECT count(*) FROM dbo.produtos_produtos")
before_import = cursor.fetchone()

contador = 1

for row in range(1, sheet.nrows):
    a = sheet.cell(row, 0).value
    b = sheet.cell(row, 1).value
    c = sheet.cell(row, 2).value
    d = sheet.cell(row, 3).value
    e = sheet.cell(row, 4).value
    f = sheet.cell(row, 5).value
    g = sheet.cell(row, 6).value
    h = sheet.cell(row, 7).value
    i = sheet.cell(row, 9).value
    j = sheet.cell(row, 11).value
    k = sheet.cell(row, 13).value
    l = sheet.cell(row, 14).value
    m = sheet.cell(row, 16).value
    ac = 'SCO'  # especificar nesse campo qual o fornecedor
    ad = 0  # especificar se os produtos tem algum desconto
    mkp1 = 1.8
    mkp2 = 1.65
    mkp3 = 1.5
    data_cadastro = date.today()

    # Assign values from each row
    values = (a, b, c, d, e, f, g, h, i, j, k, l, ac, ad, mkp1, mkp2, mkp3, data_cadastro, m, m)

    # Execute sql Query
    cursor.execute(query, values)
    print(str(contador) + " " + str(c))
    contador += 1

    # Commit the transaction
    conn.commit()

# If you want to check if all rows are imported
cursor.execute("SELECT count(*) FROM dbo.produtos_produtos")
result = cursor.fetchone()

print(('Total de Registros: ' + str(result[0] - before_import[0])))  # should be True

# Close the database connection
conn.close()