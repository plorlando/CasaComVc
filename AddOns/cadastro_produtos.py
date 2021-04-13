# Importar bibliotecas
from datetime import date
import pyodbc
import xlrd
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
file = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
print(file)

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

# file = 'd:/OneDrive/CasaComVc/Cadastro/20200630.xlsx'

# # Open the workbook and define the worksheet
book = xlrd.open_workbook(file)
sheet = book.sheet_by_name('Planilha1')
print('Sheet by names: ', book.sheet_names())

# # Open the workbook and define the worksheet

arq_excel = pd.read_excel(file, sheet_name='Planilha1')

df = pd.read_excel(file, header=0, sheet_name='Planilha1')  #, sheetname='<your sheet>'
df.to_csv('d:/OneDrive/CasaComVc/Cadastro/cadastro2.csv', index=False, quotechar="'")

query = """INSERT INTO dbo.produtos_produtos (cod_fam_forn, cod_prod_forn, produto, marca, familia_forn, sub_familia_forn,
    complemento, ean_prod, dun14, ncm, uf_origem, cidade_origem, un_venda, qtde_mult_compra, prod_larg, prod_comp,
    prod_alt, emb_larg, emb_comp, emb_alt, emb_peso, cubagem, ipi, link_forn, custo_base, custo_m2_prod,
    infos_adic, prod_med, id_forn, desconto, mkp1, mkp2, mkp3, data_cadastro)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

# grab existing row count in the database for validation later
cursor.execute("SELECT count(*) FROM dbo.produtos_produtos")
before_import = cursor.fetchone()

contador = 1

for row in range(1, sheet.nrows):
    try:
        cod_fam_forn = sheet.cell(row, 0).value  # coluna A, nvarchar(30)
        cod_prod_forn = sheet.cell(row, 1).value  # coluna B, nvarchar(30)
        produto = sheet.cell(row, 2).value  # coluna C, nvarchar(150)
        marca = sheet.cell(row, 3).value  # coluna D, nvarchar(20)
        familia_forn = sheet.cell(row, 4).value  # coluna E, nvarchar(50)
        sub_familia_forn = sheet.cell(row, 5).value  # coluna F, nvarchar(50)
        complemento = sheet.cell(row, 6).value  # coluna G, nvarchar(50)
        ean_prod = str(sheet.cell(row, 7).value).replace(' ', '').split('.')[0]  # coluna H,
        dun14 = str(sheet.cell(row, 8).value).replace(' ', '').split('.')[0]  # coluna I
        ncm = str(sheet.cell(row, 9).value).replace(' ', '').replace('.', '')  # coluna J
        uf_origem = sheet.cell(row, 10).value  # coluna K
        cidade_origem = sheet.cell(row, 11).value  # coluna L
        un_venda = sheet.cell(row, 12).value  # coluna M
        qtde_mult_compra = sheet.cell(row, 13).value  # coluna N
        prod_larg = float(round(sheet.cell(row, 14).value, 2))  # coluna O, float, prod_larg
        prod_comp = float(round(sheet.cell(row, 15).value, 2))  # coluna P, float, prod_comp
        prod_alt = float(round(sheet.cell(row, 16).value, 2))  # coluna Q, float, prod_alt
        emb_larg = float(round(sheet.cell(row, 17).value, 2))  # coluna R, float, emb_larg
        emb_comp = float(round(sheet.cell(row, 18).value, 2))  # coluna S, float, emb_comp
        emb_alt = float(round(sheet.cell(row, 19).value, 2))  # coluna T, float, emb_alt
        emb_peso = float(round(sheet.cell(row, 20).value, 2))  # coluna U, float, emb_peso
        cubagem = float(round(sheet.cell(row, 21).value, 2))  # coluna V, float, cubagem
        ipi = float(round(sheet.cell(row, 22).value, 2))  # coluna W, float, ipi
        link_forn = sheet.cell(row, 23).value  # coluna X
        custo_base = float(round(sheet.cell(row, 24).value, 2)) if sheet.cell(row, 24).value != '' else 0  # COLUNA Y
        custo_m2_prod = float(round(sheet.cell(row, 25).value, 2)) if sheet.cell(row, 25).value != '' else 0  # COLUNA Z

        infos_adic = sheet.cell(row, 26).value  # coluna AA
        ab = str(prod_larg) + ";" + str(prod_comp) + ";" + str(prod_alt)  # concatena tamanho dos produtos e salva no campo prod_med
        ac = 'CRT'  # especificar nesse campo qual o fornecedor
        ad = 0  # especificar se os produtos tem algum desconto
        mkp1 = 1.8
        mkp2 = 1.65
        mkp3 = 1.5
        data_cadastro = date.today()

        # Assign values from each row
        values = (cod_fam_forn, cod_prod_forn, produto, marca, familia_forn, sub_familia_forn, complemento, ean_prod,
                  dun14, ncm, uf_origem, cidade_origem, un_venda, qtde_mult_compra, prod_larg, prod_comp, prod_alt,
                  emb_larg, emb_comp, emb_alt, emb_peso, cubagem, ipi, link_forn, custo_base, custo_m2_prod, infos_adic,
                  ab, ac, ad, mkp1, mkp2, mkp3, data_cadastro)

        # Execute sql Query
        cursor.execute(query, values)
        print(str(contador) + " " + str(produto))
        contador += 1

        # Commit the transaction
        conn.commit()

    except Exception as e:
        print(str(e))

# If you want to check if all rows are imported
cursor.execute("SELECT count(*) FROM dbo.produtos_produtos")
result = cursor.fetchone()

print(('Total de Registros: ' + str(result[0] - before_import[0])))  # should be True

# Close the database connection
conn.close()