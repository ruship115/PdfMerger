import PyPDF2

pdfFiles = ["Deep learning.pdf", "Machine learning .pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfFiles:
    pdfFile = open(filename, 'rb')
    pdfreader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfreader)
    pdfFile.close()
merger.write('merger.pdf')
