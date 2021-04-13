from django.db import models

class Produtos(models.Model):
    # identificação
    id_casa = models.CharField(max_length=30, null=True)
    produto = models.CharField(max_length=150, null=True)
    ean_prod = models.CharField(max_length=13, null=True)
    ean_var = models.CharField(max_length=13, null=True)
    dun14 = models.CharField(max_length=14, null=True)
    ncm = models.CharField(max_length=8, null=True)
    pais_origem = models.CharField(max_length=3, null=True, default='BR')
    uf_origem = models.CharField(max_length=2, null=True)
    cidade_origem = models.CharField(max_length=100, null=True)
    descricao_html = models.TextField(null=True, blank=True)
    tags = models.CharField(max_length=256, null=True, blank=True)
    id_tray = models.IntegerField(null=True)
    id_tray_var = models.IntegerField(null=True)
    descricao_tray = models.CharField(max_length=150, null=True)
    status = models.CharField(max_length=255, null=True, default='Ativo')
    data_cadastro = models.DateField(auto_now_add=True, null=True, blank=True)

    # categorização do produto
    id_depto = models.CharField(max_length=2, null=True)
    id_cat = models.CharField(max_length=3, null=True)
    id_cat_sub = models.CharField(max_length=4, null=True)

    # Infos de cadastro no fornecedor
    id_forn = models.CharField(max_length=3, null=True)
    marca = models.CharField(max_length=20, null=True)
    cod_prod_forn = models.CharField(max_length=30, null=True)    
    cod_fam_forn = models.CharField(max_length=30, null=True)
    familia_forn = models.CharField(max_length=50, null=True)
    sub_familia_forn = models.CharField(max_length=50, null=True)
    link_forn = models.URLField(null=True)

    # infos complementares
    complemento = models.CharField(max_length=50, null=True)
    tamanho = models.CharField(max_length=50, null=True)
    cor = models.CharField(max_length=50, null=True)
    infos_adic = models.TextField(null=True)

    # infos de compra
    un_venda = models.CharField(max_length=20, null=True)
    un_compra = models.CharField(max_length=20, null=True)
    qtde_mult_compra = models.IntegerField(null=True)
    custo_base = models.FloatField(null=True)  # cadastrar preço de base do produto, a ser aplicado desconto
    custo_m2_prod = models.FloatField(null=True)
    custo_frete_compra = models.FloatField(null=True)
    desconto1 = models.FloatField(null=True, default=0)
    desconto2 = models.FloatField(null=True, default=0)

    # infos de logística
    qtde_estoque_casa = models.IntegerField(null=True, blank=True, default=0)
    qtde_estoque_forn = models.IntegerField(null=True)

    # infos ficais
    ipi = models.FloatField(null=True)

    # medidas
    prod_med = models.CharField(max_length=150, null=True)
    prod_larg = models.FloatField(null=True)
    prod_comp = models.FloatField(null=True)
    prod_alt = models.FloatField(null=True)
    emb_med = models.CharField(max_length=150, null=True)
    emb_larg = models.FloatField(null=True)
    emb_comp = models.FloatField(null=True)
    emb_alt = models.FloatField(null=True)
    emb_peso = models.FloatField(null=True)
    cubagem = models.FloatField(null=True)

    #infos de venda
    mkp1 = models.FloatField(null=True)
    mkp2 = models.FloatField(null=True)
    mkp3 = models.FloatField(null=True)
    mkp4 = models.FloatField(null=True)
    mkp5 = models.FloatField(null=True)
    mkp_mktplace = models.FloatField(null=True)
    preco_atual = models.FloatField(null=True)
    preco_oferta = models.FloatField(null=True)
    preco_boleto = models.FloatField(null=True)
    preco_venda1 = models.FloatField(null=True)
    preco_venda2 = models.FloatField(null=True)
    preco_venda3 = models.FloatField(null=True)
    preco_venda4 = models.FloatField(null=True)
    preco_venda5 = models.FloatField(null=True)
    preco_loja = models.FloatField(null=True)  # preço definido para loja
    preco_site = models.FloatField(null=True)  # preço definido para site
    preco_mktplace = models.FloatField(null=True)  # preço definido para market_place
    comissao = models.FloatField(null=True)


class BaseCompetitors(models.Model):
    id = models.AutoField(primary_key=True)
    base_url = models.URLField(null=True)
    prod_url = models.URLField(null=True)
    search = models.CharField(max_length=200, null=True)
    casa_ean = models.CharField(max_length=13, null=True)


class PriceHistory(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(null=True)
    base_url = models.URLField(null=True)
    prod_url = models.URLField(null=True)
    search = models.CharField(max_length=200, null=True)
    product_desc = models.CharField(max_length=300, null=True)
    site_prod_code = models.CharField(max_length=200, null=True)
    prod_price = models.FloatField(null=True)
    casa_ean = models.CharField(max_length=13, null=True)


class Fornecedores(models.Model):
    id = models.AutoField(primary_key=True)
    id_forn = models.CharField(max_length=3, null=True)
    fornecedor = models.CharField(max_length=100, blank=True, null=True)
    lead_time = models.IntegerField(null=True)
    desconto_base = models.FloatField(blank=True, null=True)  # utilizar para especificar um desconto que sempre será aplicado aos pedidos
    representante = models.CharField(max_length=100, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    email_rep = models.CharField(max_length=200, blank=True, null=True)
    custo_frete_compra = models.FloatField(null=True)
    custo_m2 = models.FloatField(null=True)
    pedido_minimo = models.FloatField(null=True)
    data_ult_preco = models.DateField(null=True)