import os
import cv2
from PIL import Image

diretorio = 'D:/OneDrive/CasaComVc/Sistemas/CasaComVc Scrapping/Scrapping/Images/convert/'
listagem = os.listdir(diretorio)

for i in listagem:
    arquivo = diretorio + i
    base = os.path.basename(arquivo)
    img = Image.open(arquivo)
    width, height = img.size
    print(arquivo + ", Width Original: " + str(width) + ", Height Original: " + str(height))
    (new_width, new_height) = (width/4, height/4)
    img = img.resize((round(new_width), round(new_height)), Image.ANTIALIAS)
    # img.save(arquivo, format='jpeg')




