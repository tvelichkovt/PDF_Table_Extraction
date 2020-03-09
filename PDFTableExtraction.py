#https://drive.google.com/drive/folders/1xjutthFIQ137VYSiDXBX6YtMUkt2sRoO

import tabula
from tabula import read_pdf

#1. Local fetch
pdf_path = 'sample_table.pdf' #local patch
tabula.read_pdf(pdf_path, pages="all", stream=True) #all pages

#tabula.read_pdf(pdf_path, pages="1", stream=True) #specific pages
#tabula.read_pdf(pdf_path, pages=3, stream=True)[0] 
#tabula.read_pdf(pdf_path, pages="1-2,3", stream=True) #specific pages
#tabula.read_pdf(pdf_path, pages="all", stream=True, output_format="json") #all pages into JSON, TSV, or CSV
#tabula.convert_into(pdf_path, "test.json", output_format="json") ..or convert




#1. Link fetch
#pdf_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

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



     


