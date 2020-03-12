'''
#https://drive.google.com/drive/folders/1xjutthFIQ137VYSiDXBX6YtMUkt2sRoO
#import os ; cwd = os.getcwd(); files = os.listdir(cwd) ; print("Files in %r: %s" % (cwd, files)) 

'''

# 1. Imports & Sample Files
import tabula
from tabula import read_pdf

pdf_file1 = "https://github.com/tvelichkovt/PDF_Table_Extraction/raw/master/Sample_Files/PDFTableExtraction_Small_Table.pdf"
pdf_file2 = "https://github.com/tvelichkovt/PDF_Table_Extraction/raw/master/Sample_Files/PDFTableExtraction_Tesla_Bonds.pdf"
pdf_file3 = "https://github.com/tvelichkovt/PDF_Table_Extraction/raw/master/Sample_Files/PDFTableExtraction_World_GDP.pdf"
pdf_file4 = "https://databank.worldbank.org/data/download/GDP.pdf"

# 2. Read PDFs

tabula.read_pdf(pdf_file1, pages="all", stream=True)[0] # read all pages
tabula.read_pdf(pdf_file2, pages=1, stream=True)[0] # read 1 page
tabula.read_pdf(pdf_file3, pages="1-2", stream=True)[0] #specific pages

tabula.convert_into(pdf_file1, "PDFTableExtraction_Output.csv", output_format="csv") # extract into file JSON, TSV, or CSV
tabula.convert_into(pdf_file2, "PDFTableExtraction_Output.json", output_format="json")



     


