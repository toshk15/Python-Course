from PyPDF2 import PdfFileWriter, PdfFileReader
pages_to_delete = [3, 4, 5] # page numbering starts from 0
infile = PdfFileReader('1.pdf', 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i not in pages_to_delete:
        p = infile.getPage(i)
        output.addPage(p)

with open('ine.pdf', 'wb') as f:
    output.write(f)
