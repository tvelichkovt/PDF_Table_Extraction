#pip install camelot-py[all],click;matplotlib;numpy;opencv-python;openpyxl;pandas;pdfminer.six;PyPDF2



import camelot
tables = camelot.read_pdf('C:\@\T\git\PDF_Table_Extraction\foo.pdf')
tables

tables.export('foo.csv', f='csv', compress=True) # json, excel, html


tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}
tables[0].to_csv('foo.csv') # to_json, to_excel, to_html
tables[0].df # get a pandas DataFrame!