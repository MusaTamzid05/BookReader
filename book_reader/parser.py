from PyPDF2 import PdfFileReader

class PDFParser:

    def __init__(self , path):

        self.reader_obj = None

        with open(path , "rb") as f:
            print("PDF reader object is {}".format(self.reader_obj))
            print("Number of Pages : {}".format(self.reader_obj.getNumPages()))
            print("Title : {}".format(self.reader_obj.getDocumentInfo().title))
            print("Author : {}".format(self.reader_obj.getDocumentInfo().author))

