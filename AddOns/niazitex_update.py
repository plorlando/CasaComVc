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
book = xlrd.open_workbook('d:/OneDrive/CasaComVc/Modelos/niazitex.xlsx')
sheet = book.sheet_by_name('Estoque')
# print('Sheet by names: ', book.sheet_names())

query = """UPDATE dbo.produtos_produtos
           SET custo_base = ?, qtde_estoque_forn = ?, ipi = 0
           WHERE cod_prod_forn = ?"""

contador = 1

for row in range(1, sheet.nrows):
    cod_prod_forn = sheet.cell(row, 0).value
    price = sheet.cell(row, 3).value
    estoque = sheet.cell(row, 4).value

    # Assign values from each row
    values = (price, estoque, cod_prod_forn)

    select = """SELECT id FROM dbo.produtos_produtos WHERE cod_prod_forn = ?"""
    cursor.execute(select, (cod_prod_forn,))
    resultado = cursor.fetchone()

    if resultado != None:
        # Execute sql Query
        cursor.execute(query, values)
        # Commit the transaction
        conn.commit()
        print(str(contador) + " " + "ID: " + str(cod_prod_forn) + " - PREÇO: " + str(price) + " - ESTOQUE: " + str(estoque) + " - ATUALIZADO!")
    else:
        print(str(contador) + " " + "ID: " + str(cod_prod_forn) + " - PREÇO: " + str(price) + " - ESTOQUE: " + str(estoque) + " - CÓDIGO NÃO ENCONTRADO")

    # try:
    #     # Execute sql Query
    #     cursor.execute(query, values)
    #
    #     # Commit the transaction
    #     conn.commit()
    #
    #     print(str(contador) + " " + "ID: " + str(cod_prod_forn) + " - PREÇO: " + str(price) + " - ESTOQUE: " + str(estoque) + " - ATUALIZADO!")
    #
    # except:
    #     print(str(contador) + " " + "ID: " + str(cod_prod_forn) + " - PREÇO: " + str(price) + " - ESTOQUE: " + str(estoque) + " - CÓDIGO NÃO ENCONTRADO")

    contador += 1

# Close the database connection
conn.close()