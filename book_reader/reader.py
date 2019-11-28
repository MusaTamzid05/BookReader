from .parser import PDFParser
from .speaker import speak
from .speaker import TEMP_PATH
import os


class Reader:

    def __init__(self ,  path):

        self.parser = None

        try:
            self.parser = PDFParser(path)
        except FileNotFoundError:
            print("PDF {} could not be found.".format(path))

    def close(self):
        self.parser.close()

        if os.path.isfile(TEMP_PATH):
            os.remove(TEMP_PATH)



    def read_from(self , page_num):

        if self.parser is None:
            print("No parser.Initialize with a valid pdf first!!")
            return

        sentences = self.parser.get_sentences_from(page_num)

        if sentences is None:
            print("No sentences to read from")
            return

        readable_sentences = self.parser.get_clear_sentences(sentences)
        for sentence in readable_sentences:
            if speak(sentence , print_sentence = True) == False:
                print("Every sentence are not read")
                break

        self.parser.close()







