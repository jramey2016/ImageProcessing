import PyPDF2
import sys

inputs = sys.argv[1:]

#Merging Pdf's
def pdf_merge(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('combined.pdf')

pdf_merge(inputs)

joinPDF = PyPDF2.PdfFileReader(open('combined.pdf', 'rb'))
watermarkPDF = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
join_watermarkPDF = PyPDF2.PdfFileWriter()

for i in range(joinPDF.getNumPages()):
    page = joinPDF.getPage(i)
    page.mergePage(watermarkPDF.getPage(0))
    join_watermarkPDF.addPage(page)

    with open('watermark_output.pdf', 'wb') as my_watermark:
        join_watermarkPDF.write(my_watermark)
