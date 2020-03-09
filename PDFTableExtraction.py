#https://drive.google.com/drive/folders/1xjutthFIQ137VYSiDXBX6YtMUkt2sRoO

#pip install tabula-py
#pip install -q tabula-py

#be carefil with JAVA path, C:\Program Files (x86)\Java\jre1.8.0_241\bin ; "https://www.java.com/en/download/help/path.xml"

import tabula
from tabula import read_pdf

#link fetch
pdf_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

#local fetch
#pdf_path = 'foo.pdf' #local patch

tabula.read_pdf(pdf_path, pages="1", stream=True) #specific pages

#tabula.read_pdf(pdf_path, pages=3, stream=True)[0] 
#tabula.read_pdf(pdf_path, pages="1-2,3", stream=True) #specific pages
#tabula.read_pdf(pdf_path, pages="all", stream=True) #all pages


#read pdf as JSON, TSV, or CSV
#tabula.read_pdf(pdf_path, output_format="json")


#convert from pdf into JSON, CSV, TSV
tabula.convert_into(pdf_path, "test.json", output_format="json")

import json

with open('test.json') as f:
  data = json.load(f)

print(data)



#===


pdf_path3 = "https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/spanning_cells.pdf"
tabula.read_pdf(
    pdf_path3,
    pages="1",
    lattice=True,
    pandas_options={"header": [0, 1]},
    area=[0, 0, 50, 100],
    relative_area=True,
    multiple_tables=False,
)[0]



template_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.tabula-template.json"
tabula.read_pdf_with_template(pdf_path, template_path)



     


