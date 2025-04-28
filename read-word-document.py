#Import library
from docx import Document
# Load the Word document
#doc = open("word-document.docx","rb")
doc = Document("word-document.docx")

# create an empty string and call this document. This document 
#variable store each paragraph in the Word document.We then 
#create a for loop that goes through each paragraph in the Word 
#document and appends the paragraph.
docu=""
for para in doc.paragraphs:
    docu += para.text
#to see the output call docu
print(docu)