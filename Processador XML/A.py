#Processador de XML usando ElementTree (DOM)

import os
from xml.etree import ElementTree

arquivo = open("autores.xml", "a")
file = 'Busca-e-Minera-o-de-Textos\data\cf79.xml'

dom = ElementTree.parse(file)

record = dom.findall('RECORD/AUTHORS/AUTHOR')

arquivo.write('<authors>')
for c in record:
    author = c.text
    arquivo.write('<author>{}</author> \n'.format(author))
    
arquivo.write('</authors>')
    
    