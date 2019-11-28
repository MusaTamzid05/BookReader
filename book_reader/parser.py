from PyPDF2 import PdfFileReader
from nltk import sent_tokenize



class PDFParser:

    def __init__(self , path):


        self.reader_obj = None
        self.num_page = -1
        self.f_ptr = open(path , "rb")

        self.reader_obj = PdfFileReader(self.f_ptr)
        self.total_pages = self.reader_obj.getNumPages()





    def get_text_from(self , page_num):

        page = self.reader_obj.getPage(page_num)
        return page.extractText()

    def show_info(self):
        print("Number of Pages : {}".format(self.total_pages))
        print("Title : {}".format(self.reader_obj.getDocumentInfo().title))
        print("Author : {}".format(self.reader_obj.getDocumentInfo().author))

        print("Book Outlines")
        self.get_text_from(10)

    def close(self):
        self.f_ptr.close()

    def get_tokenize_sentences(self , text):
        return sent_tokenize(text)

    def get_sentences_from(self , page_num):

        if page_num < 0 and page_num > self.total_pages:
            print("Invalid page num : {}".format(page_num))
            return None


        text = self.get_text_from(page_num)
        return self.get_tokenize_sentences(text)

    def clear(self , sentence):

        ignore_charecters = ["™" , "˜" , "?" , "!" , "(" , ")" , "˚" , "." , "-"]
        new_sentence = ""

        for ch in sentence:
            if ch in ignore_charecters:
                continue

            elif ch == "%":
                ch = " percent "
            new_sentence += ch

        return new_sentence


    def get_clear_sentences(self , sentences):

        cleared_sentences = []

        for sentence in sentences:
            temp_sentence = self.clear(sentence)

            if "," in temp_sentence:
                temp_sentences = temp_sentence.split(",")
            else:
                temp_sentences = [temp_sentence]

            for t_sentence in temp_sentences:
                cleared_sentences.append(t_sentence.strip())

        return cleared_sentences


