from django.db import models
from django.db.models.fields import FloatField

class NFe(models.Model):
    # infos de classificação
    es = models.CharField(max_length=1)  # classificar se a nota é de entrada ou saida
    tipo_nota =  models.CharField(max_length=4)  # classificar se é NFCe ou NFe

    # cadeçalho da nota
    infNFe_ide_xnlns = models.CharField(max_length=256)
    infNFe_ide_infNFeId = models.CharField(max_length=256)
    infNFe_ide_infNFeversao = models.CharField(max_length=20)
    infNFe_ide_cUF = models.CharField(max_length=2)
    infNFe_ide_cNF = models.CharField(max_length=12)
    infNFe_ide_natOp = models.CharField(max_length=100)
    infNFe_ide_mod = models.CharField(max_length=2)
    infNFe_ide_serie = models.CharField(max_length=3)
    infNFe_ide_nNF = models.CharField(max_length=10)
    infNFe_ide_dhEmi = models.DateTimeField()
    infNFe_ide_dhSaiEnt = models.DateTimeField()
    infNFe_ide_tpNF = models.CharField(max_length=3)
    infNFe_ide_idDest = models.CharField(max_length=3)
    infNFe_ide_cMunFG = models.CharField(max_length=10)
    infNFe_ide_tpImp = models.CharField(max_length=2)
    infNFe_ide_tpEmis = models.CharField(max_length=2)
    infNFe_ide_cDV = models.CharField(max_length=3)
    infNFe_ide_tpAmb = models.CharField(max_length=2)
    infNFe_ide_finNFe = models.CharField(max_length=2)
    infNFe_ide_indFinal = models.CharField(max_length=2)
    infNFe_ide_indPres = models.CharField(max_length=2)
    infNFe_ide_procEmi = models.CharField(max_length=2)
    infNFe_ide_verProc = models.CharField(max_length=15)

    # infos emissor
    infNFe_emit_CNPJ = models.CharField(max_length=14)
    infNFe_emit_xNome = models.CharField(max_length=256)
    infNFe_emit_xFant = models.CharField(max_length=256)
    infNFe_emit_xLgr = models.CharField(max_length=256)
    infNFe_emit_nro = models.PositiveIntegerField()
    infNFe_emit_xBairro = models.CharField(max_length=100)
    infNFe_emit_cMun = models.CharField(max_length=10)
    infNFe_emit_xMun = models.CharField(max_length=100)
    infNFe_emit_UF = models.CharField(max_length=2)
    infNFe_emit_CEP = models.CharField(max_length=8)
    infNFe_emit_cPais = models.CharField(max_length=4)
    infNFe_emit_xPais = models.CharField(max_length=100)
    infNFe_emit_fone = models.CharField(max_length=15)
    infNFe_emit_IE = models.CharField(max_length=9)
    infNFe_emit_CRT = models.CharField(max_length=1)
    
    # infos dest


    # itens det
    infNFe_det_nItem = models.IntegerField()
    infNFe_det_cProd = models.CharField(max_length=50)
    infNFe_det_cEAN = models.CharField(max_length=13)
    infNFe_det_xProd = models.CharField(max_length=256)
    infNFe_det_NCM = models.CharField(max_length=8)
    infNFe_det_CFOP = models.CharField(max_length=4)
    infNFe_det_uCom = models.CharField(max_length=3)
    infNFe_det_qCom = models.IntegerField()
    infNFe_det_vUnCom = models.FloatField()
    infNFe_det_vProd = models.FloatField()
    infNFe_det_cEANTrib = models.CharField(max_length=13)
    infNFe_det_uTrib = models.CharField(max_length=3)
    infNFe_det_qTrib = models.IntegerField()
    infNFe_det_vUnTrib = models.FloatField()
    infNFe_det_vFrete = models.FloatField()
    infNFe_det_indTot = models.IntegerField()
    infNFe_det_nItemPed = models.IntegerField()
    infNFe_det_ICMS_orig = models.CharField(max_length=1)
    infNFe_det_ICMS_CSOSN = models.CharField(max_length=3)
    infNFe_det_PIS_CST = models.CharField(max_length=2)
    infNFe_det_COFINS_CST = models.CharField(max_length=2)

    # informações de totalização da nota
    total_ICMSTot_vBC = models.FloatField()
    total_ICMSTot_vICMS = models.FloatField()
    total_ICMSTot_vICMSDeson = models.FloatField()
    total_ICMSTot_vFCP = models.FloatField()
    total_ICMSTot_vBCST = models.FloatField()
    total_ICMSTot_vST = models.FloatField()
    total_ICMSTot_vFCPST = models.FloatField()
    total_ICMSTot_vFCPSTRet = models.FloatField()
    total_ICMSTot_vProd = models.FloatField()
    total_ICMSTot_vFrete = models.FloatField()
    total_ICMSTot_vSeg = models.FloatField()
    total_ICMSTot_vDesc = models.FloatField()
    total_ICMSTot_vII = models.FloatField()
    total_ICMSTot_vIPI = models.FloatField()
    total_ICMSTot_vPIS = models.FloatField()
    total_ICMSTot_vCOFINS = models.FloatField()
    total_ICMSTot_vOutro = models.FloatField()
    total_ICMSTot_vNF = models.FloatField()

    # informações de transporte
    transp_modFrete = models.CharField(max_length=1)
    transp_esp = models.CharField(max_length=15)
    transp_pesoL = models.FloatField()
    transp_pesoB = models.FloatField()

    # informações de pagamento
    pag_detPag_tPag = models.IntegerField()
    pag_detPag_vPag = models.FloatField()

    # informações adicionais
    infRespTec_CNPJ = models.CharField(max_length=15)
    infRespTec_xContato = models.CharField(max_length=100)
    infRespTec_email = models.EmailField()
    infRespTec_fone = models.CharField(max_length=13)

    # signature
    signature_xmlns = models.CharField(max_length=256)
    signature_signedInfo_CanonicalizationMethod = models.CharField(max_length=256)
    signature_signedInfo_SignatureMethod = models.CharField(max_length=256)
    signature_signedInfo_Reference_URI = models.CharField(max_length=256)
    signature_signedInfo_Reference_Transform1 = models.CharField(max_length=256)
    signature_signedInfo_Reference_Transform2 = models.CharField(max_length=256)
    signature_signedInfo_Reference_DigestMethod = models.CharField(max_length=256)
    signature_signedInfo_Reference_DigestValue = models.CharField(max_length=256)
    signature_SignatureValue = models.TextField()
    signature_KeyInfo_X509Certificate = models.TextField()

    # informaçõs de proteção da nota
    protNFe = models.CharField(max_length=20)
    protNFe_infProt_tpAmb = models.CharField(max_length=1)
    protNFe_infProt_verAplic = models.CharField(max_length=30)
    protNFe_infProt_chNFe = models.CharField(max_length=44)
    protNFe_infProt_dhRecbto = models.DateTimeField()
    protNFe_infProt_nProt = models.CharField(max_length=15)
    protNFe_infProt_digVal = models.CharField(max_length=28)
    protNFe_infProt_cStat = models.CharField(max_length=3)
    protNFe_infProt_xMotivo = models.CharField(max_length=100)