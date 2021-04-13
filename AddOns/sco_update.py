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
book = xlrd.open_workbook('d:/OneDrive/CasaComVc/Modelos/sco.xlsx')
sheet = book.sheet_by_name('Sheet1')
# print('Sheet by names: ', book.sheet_names())

query = """UPDATE dbo.produtos_produtos
           SET custo_m2_prod = ?, qtde_estoque_forn = ?, cod_adicional = ?
           WHERE ean_prod = ? AND id_forn = 'SCO'"""

contador = 1
atualizado = 0
falha = 0

for row in range(1, sheet.nrows):
    ean_prod = sheet.cell(row, 0).value
    price = round(sheet.cell(row, 11).value / sheet.cell(row, 8).value, 2)
    estoque = sheet.cell(row, 9).value
    cod_adicional = sheet.cell(row, 13).value

    # Assign values from each row
    values = (price, estoque, cod_adicional, ean_prod)

    select = """SELECT id FROM dbo.produtos_produtos WHERE ean_prod = ?"""
    cursor.execute(select, (ean_prod,))
    resultado = cursor.fetchone()

    if resultado != None:
        cursor.execute(query, values)
        conn.commit()
        print(str(contador) + " " + "EAN: " + str(ean_prod) + " - PREÇO: " + str(price) + " - ESTOQUE: " + str(estoque) + " - CÓDIGO ADICIONAL: " + str(cod_adicional) + " - ATUALIZADO!")
        atualizado += 1
    else:
        print(str(contador) + " " + "EAN: " + str(ean_prod) + " - PREÇO: " + str(price) + " - ESTOQUE: " + str(estoque) + " - CÓDIGO ADICIONAL: " + str(cod_adicional) + " - CÓDIGO NÃO ENCONTRADO")
        falha += 1

    contador += 1

# Close the database connection
print("Atualizado: " + str(atualizado))
print("Falha: " + str(falha))
conn.close()