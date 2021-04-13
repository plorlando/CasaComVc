import lxml.html as parser
import requests
import datetime


def TapetesNaWeb(cursor, conn, sql_insert):
    sql = "SELECT prod_url, casa_ean FROM dbo.produtos_basecompetitors WHERE base_url = 'http://www.tapetesnaweb.com.br'"
    cursor.execute(sql)
    result = cursor.fetchall()
    tnw_product_desc = "//span[@id='lblNome']/text()"
    tnw_product_code = "//span[@id='lblCodigoProduto']/text()"
    tnw_product_price = "//p[@class='txt2']/text()"
    tnw_base_url = "www.tapetesnaweb.com.br"
    contador_falha = 0
    contador_sucesso = 0
    data_atualiz = datetime.datetime.now()

    for i in result:
        product_url = i[0]
        casa_ean = i[1]
        r = requests.get(product_url)
        html = parser.fromstring(r.text)
        prod = html.xpath(tnw_product_desc)
        cod = html.xpath(tnw_product_code)
        p = html.xpath(tnw_product_price)

        if prod:
            produto = str(prod).replace("'['", "").replace("']'", "").replace("[", "").replace("]", "")
            codigo = str(cod).replace("'['", "").replace("']'", "").replace("[", "").replace("]", "")
            preco = float(str(p[0]).replace("R$ ", "").replace(".", "").replace(",", "."))
            contador_sucesso += 1
        else:
            produto = ""
            codigo = ""
            preco = 0
            contador_falha += 1

        print(produto)
        print(codigo)
        print(preco)
        print(product_url)
        print("SUCESSO: " + str(contador_sucesso))
        print("FALHA: " + str(contador_falha))
        print("TOTAL PROCESSADO: " + str(contador_falha+contador_sucesso))

        values = (data_atualiz, str(product_url), produto, codigo, preco, str(tnw_base_url), casa_ean)
        cursor.execute(sql_insert, values)
        conn.commit()

        print("------PRODUTO FINALIZADO------")


    sql_count = "SELECT count(prod_url) as sql_count FROM dbo.produtos_basecompetitors WHERE base_url = " \
                "'http://www.tapetesnaweb.com.br'"
    cursor.execute(sql_count)
    result_count = cursor.fetchone()
    print("Total de registros do SELECT: " + str(result_count))



def LojasDonna(cursor, conn, sql_insert):
    sql = "SELECT prodUrl, casaEan FROM dbo.produtos_basecompetitors WHERE baseUrl = 'https://www.lojasdonna.com.br/'"
    cursor.execute(sql)
    result = cursor.fetchall()
    ljd_product_desc = "//span[@id='lblNome']/text()"
    ljd_product_code = "//span[@id='lblCodigoProduto']/text()"
    ljd_product_price = "//html/body/form/div[3]/div[3]/div/div/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/span[3]/strong/text()"
    ljd_base_url = "www.lojasdonna.com.br"
    contador_falha = 0
    contador_sucesso = 0
    data_atualiz = datetime.datetime.now()

    for i in result:
        product_url = i[0]
        casa_ean = i[1]
        r = requests.get(product_url)
        html = parser.fromstring(r.text)
        prod = html.xpath(ljd_product_desc)
        cod = html.xpath(ljd_product_code)
        p = html.xpath(ljd_product_price)
        print(product_url)
        print(p)
        p = str(p)

        if prod:
            produto = str(prod).replace("'['", "").replace("']'", "").replace("[", "").replace("]", "")
            codigo = str(cod).replace("'['", "").replace("']'", "").replace("[", "").replace("]", "")
            preco = float(str(p).replace("R$ ", "").replace(".", "").replace(",", ".").replace("['", "").replace("']", ""))
            contador_sucesso += 1
        else:
            produto = ""
            codigo = ""
            preco = 0
            contador_falha += 1

        print(produto)
        print(codigo)
        print(preco)
        print(product_url)
        print("SUCESSO: " + str(contador_sucesso))
        print("FALHA: " + str(contador_falha))
        print("TOTAL PROCESSADO: " + str(contador_falha + contador_sucesso))

        # values = (data_atualiz, str(product_url), produto, codigo, preco, str(ljd_base_url), casa_ean)
        # cursor.execute(sql_insert, values)
        # conn.commit()

        print("------PRODUTO FINALIZADO------")

    sql_count = "SELECT count(baseUrl) as sql_count FROM dbo.produtos_basecompetitors WHERE baseUrl = " \
                "'http://www.lojasdonna.com.br'"
    cursor.execute(sql_count)
    result_count = cursor.fetchone()
    print("Total de registros do SELECT: " + str(result_count))


def MadeiraMadeira(cursor, conn, sql_insert):
    sql = "SELECT prod_url, casa_ean FROM dbo.produtos_basecompetitors WHERE base_url = " \
          "'https://www.madeiramadeira.com.br' AND search = 'niazitex'"
    cursor.execute(sql)
    result = cursor.fetchall()
    mm_product_desc = "//h1[@class='title is-medium product-title']/text()"
    mm_product_code = "//span[@class='reference-block__item']/text()"
    mm_product_price = "/html/body/main/div[2]/div/div/section[1]/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/p[3]/span[2]/span[1]/strong/text()"
    mm_base_url = "https://www.madeiramadeira.com.br"
    contador_falha = 0
    contador_sucesso = 0
    data_atualiz = datetime.datetime.now()

    for i in result:
        product_url = i[0]
        casa_ean = i[1]
        r = requests.get(product_url)
        html = parser.fromstring(r.text)
        prod = html.xpath(mm_product_desc)
        cod = html.xpath(mm_product_code)
        p = html.xpath(mm_product_price)
        print(product_url)
        print(prod)
        print(cod)
        print(p)


        if prod and cod and p:
            produto = str(prod).replace("['", "").replace("']", "").replace("\\n", "").strip()
            codigo = str(cod).replace("['", "").replace("']", "").replace("\\n", "").replace("Identificador:", "").strip()
            preco = float(str(p[0]).replace(".", "").replace(",", "."))
            contador_sucesso += 1
        else:
            produto = ""
            codigo = ""
            preco = 0
            contador_falha += 1

        print(produto)
        print(codigo)
        print(preco)
        print(product_url)
        print("SUCESSO: " + str(contador_sucesso))
        print("FALHA: " + str(contador_falha))
        print("TOTAL PROCESSADO: " + str(contador_falha + contador_sucesso))

        values = (data_atualiz, str(product_url), produto, codigo, preco, str(mm_base_url), casa_ean)
        cursor.execute(sql_insert, values)
        conn.commit()

        print("------PRODUTO FINALIZADO------")

    sql_count = "SELECT count(base_url) as sql_count FROM dbo.produtos_basecompetitors WHERE base_url = " \
                "'https://www.madeiramadeira.com.br'"
    cursor.execute(sql_count)
    result_count = cursor.fetchone()
    print("Total de registros do SELECT: " + str(result_count))


def WPHome(cursor, conn, sql_insert):
    sql = "SELECT prod_url, casa_ean FROM dbo.produtos_basecompetitors WHERE base_url = " \
          "'https://www.wphome.com.br/'"
    cursor.execute(sql)
    result = cursor.fetchall()
    product_desc = "//h1[@class='title is-medium product-title']/text()"
    product_code = "//span[@class='reference-block__item']/text()"
    product_price = "/html/body/main/div[2]/div/div/section[1]/div[2]/div[3]/div[1]/div[2]/div/div/div[2]/p[3]/span[2]/span[1]/strong/text()"
    base_url = "https://www.wphome.com.br/"
    contador_falha = 0
    contador_sucesso = 0
    data_atualiz = datetime.datetime.now()

    for i in result:
        product_url = i[0]
        casa_ean = i[1]
        r = requests.get(product_url)
        html = parser.fromstring(r.text)
        prod = html.xpath(product_desc)
        cod = html.xpath(product_code)
        p = html.xpath(product_price)
        print(product_url)
        print(prod)
        print(cod)
        print(p)


        if prod and cod and p:
            produto = str(prod).replace("['", "").replace("']", "").replace("\\n", "").strip()
            codigo = str(cod).replace("['", "").replace("']", "").replace("\\n", "").replace("Identificador:", "").strip()
            preco = float(str(p[0]).replace(".", "").replace(",", "."))
            contador_sucesso += 1
        else:
            produto = ""
            codigo = ""
            preco = 0
            contador_falha += 1

        print(produto)
        print(codigo)
        print(preco)
        print(product_url)
        print("SUCESSO: " + str(contador_sucesso))
        print("FALHA: " + str(contador_falha))
        print("TOTAL PROCESSADO: " + str(contador_falha + contador_sucesso))

        values = (data_atualiz, str(product_url), produto, codigo, preco, str(base_url), casa_ean)
        cursor.execute(sql_insert, values)
        conn.commit()

        print("------PRODUTO FINALIZADO------")

    sql_count = "SELECT count(base_url) as sql_count FROM dbo.produtos_basecompetitors WHERE base_url = " \
                "'https://www.wphome.com.br/'"
    cursor.execute(sql_count)
    result_count = cursor.fetchone()
    print("Total de registros do SELECT: " + str(result_count))