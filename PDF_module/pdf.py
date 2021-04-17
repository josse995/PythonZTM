import PyPDF2
import sys

inputs = sys.argv[1:]


def rotatePage():

    with open('dummy.pdf', 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('tilt.pdf', 'wb') as newFile:
            writer.write(newFile)


def mergePdfs(pdfList):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfList:
        print(pdf)
        merger.append(pdf)
    merger.write('super_pdf.pdf')


def watermark():
    template = PyPDF2.PdfFileReader(open('super_pdf.pdf', 'rb'))
    watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
    output = PyPDF2.PdfFileWriter()
    for i in range(template.numPages):
        page = template.getPage(i)
        page.mergePage(watermark.getPage(0))
        output.addPage(page)

        with open('watermarked_output.pdf', 'wb') as file:
            output.write(file)
