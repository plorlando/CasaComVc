import xml.etree.ElementTree as ET
import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
file = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
print(file)
tree = ET.parse(file)
root = tree.getroot()

ns = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
nodefind = root.find('{http://www.portalfiscal.inf.br/nfe}NFe/{http://www.portalfiscal.inf.br/nfe}infNFe/{http://www.portalfiscal.inf.br/nfe}ide/{http://www.portalfiscal.inf.br/nfe}cNF')
# print(nodefind)
# print(nodefind.text)




count_det = 1
for det in root.findall('.//nfe:det', ns):
    nItem = det.attrib['nItem']
    print(nItem)
    print(count_det)
    count_det += 1
    print(det.attrib)
