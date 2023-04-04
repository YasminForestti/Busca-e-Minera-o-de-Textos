#Processador de XML usando Minidom

import xml.dom.minidom as dom

document = dom.parse("Busca-e-Minera-o-de-Textos\data\cf79.xml").documentElement

with open("titulo.xml", "w") as file:
    file.write('<titles>')
    for title in document.getElementsByTagName("TITLE"):
    
        text = title.firstChild.nodeValue

        text = text.replace('\n', ' ')
        file.write('<title>{}</title> \n'.format(text))
    file.write('</titles>')
