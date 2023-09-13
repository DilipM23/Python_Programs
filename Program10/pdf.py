from PyPDF2 import PdfReader, PdfWriter

num1 = int(input("Enter the page number of the first pdf"))
num2 = int(input("Enter the page number of the second page"))
pdf1 = open("D:\\Dilip\\OS Notes\\Module 1.pdf", 'rb')
pdf2 = open("D:\Dilip\OS Notes\Module 2.pdf", 'rb')

pdf_writer = PdfWriter()

pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages[num1-1]
pdf_writer.add_page(page)

pdf2_reader = PdfReader(pdf2)
page = pdf2_reader.pages[num2-1]
pdf_writer.add_page(page)

with open("PDF.pdf","wb") as output :
    pdf_writer.write(output)

print("PDF combined successfully")