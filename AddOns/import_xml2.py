import xml.etree.ElementTree as ET
import requests
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
file = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
print(file)
tree = ET.parse(file)
root = tree.getroot()

filtro = '*'

print(root[0][0][4].text)


# for child in root:
#     print(child.tag, child.attrib)

# for child in root.iter(filtro):
#     print(child.tag, child.attrib)