'''
#https://drive.google.com/drive/folders/1xjutthFIQ137VYSiDXBX6YtMUkt2sRoO
#import os ; cwd = os.getcwd(); files = os.listdir(cwd) ; print("Files in %r: %s" % (cwd, files)) 

'''

# 1. Imports
import tabula
from tabula import read_pdf

# 2. Local fetch
pdf_file = 'PDFTableExtraction small table.pdf' #local patch
tabula.read_pdf(pdf_file, pages="all", stream=True) #all pages
tabula.convert_into(pdf_file, "PDFTableExtraction output.csv", output_format="csv")
pdf_file = 'PDFTableExtraction Tesla Convertable Bonds.pdf' #local patch
tabula.read_pdf(pdf_file, pages="1", stream=True) #specific pages
tabula.convert_into(pdf_file, "PDFTableExtraction output.json", output_format="json")

#tabula.read_pdf(pdf_file, pages=3, stream=True)[0] 
#tabula.read_pdf(pdf_file, pages="1-2,3", stream=True) #specific pages
#tabula.read_pdf(pdf_file, pages="all", stream=True, output_format="json") #all pages into JSON, TSV, or CSV
#tabula.convert_into(pdf_file, "test.json", output_format="json") ..or convert

#3. www link fetch
import tabula
from tabula import read_pdf

pdf_file_link = "http://www3.weforum.org/docs/GCR2017-2018/05FullReport/TheGlobalCompetitivenessReport2017%E2%80%932018.pdf"

tabula.read_pdf(
    pdf_file_link,
    pages="11",
    lattice=True,
    pandas_options={"header": [0, 1]},
    area=[0, 0, 50, 100],
    relative_area=True,
    multiple_tables=False,
)[0]



template_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.tabula-template.json"
tabula.read_pdf_with_template(pdf_file_link, template_path)



     


