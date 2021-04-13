import os
from PIL import Image

diretorio = 'D:/OneDrive/CasaComVc/Sistemas/CasaComVc Scrapping/Scrapping/Images/convert/'
listagem = os.listdir(diretorio)

for i in listagem:
    arquivo = diretorio + i
    base = os.path.basename(arquivo)
    print(os.path.splitext(base)[0])
    im = Image.open(arquivo).convert("RGB")
    im.save(diretorio + os.path.splitext(base)[0] + '.jpg', "jpeg", quality=100)

