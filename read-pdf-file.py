import PyPDF2
from PyPDF2 import PdfFileReader
 
#Creating a pdf file object
pdf = open("resume.pdf","rb")

#creating pdf reader object
pdf_reader = PyPDF2.PdfReader(pdf)

#checking number of pages in a pdf file
num_pages = len(pdf_reader.pages)
print(f"Number of pages: {num_pages}")

#creating a page object
page = pdf_reader.pages[0]

#finally extracting text from the page
#print(page.extractText())
first_page = pdf_reader.pages[0]
text = first_page.extract_text()
print(text)

#closing the pdf file
pdf.close() 
#keep window open & closes only if user press enter button
input("\nPress Enter to exit...")