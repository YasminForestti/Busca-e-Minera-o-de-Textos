import os
import xml.etree.ElementTree as ET
import string

def parse_xml_file(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    docs = []
    for record in root.findall("./RECORD"):
        doc_id = record.find("./RECORDNUM").text
        abstract = record.find("./ABSTRACT")
        if abstract is None:
            abstract = record.find("./EXTRACT")
        if abstract is not None:
            doc_text = abstract.text.strip()
            doc_text = doc_text.translate(str.maketrans("", "", string.punctuation)).upper()
            docs.append((doc_id, doc_text))
    
    return docs

def create_inverted_index(documents):
    inverted_index = {}
    for doc_id, doc_text in documents:
        for word in doc_text.split():
            if word not in inverted_index:
                inverted_index[word] = [doc_id]
            else:
                inverted_index[word].append(doc_id)

    return inverted_index

def write_inverted_index_to_file(inverted_index, output_file):
    with open(output_file, "w") as f:
        for word, docs in inverted_index.items():
            line = word + " ; " + str(docs) + "\n"
            f.write(line)

def main():
    GLI_path  = 'SRM/Indexador/GLI.cfg'
    input_files = []
    output_file = None
    with open(GLI_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("LEIA="):
                input_files.append(line[len("LEIA="):])
            elif line.startswith("ESCREVA="):
                output_file = line[len("ESCREVA="):]          
    documents = []
    for input_file in input_files:
        documents += parse_xml_file(input_file)
    inverted_index = create_inverted_index(documents)

    write_inverted_index_to_file(inverted_index, output_file)
main()