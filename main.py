from book_reader.speaker import speak
from book_reader.parser import PDFParser

def main():
    #speak("This is a message.")

    pdf_parser = PDFParser(path = "/home/musa/Downloads/design-web-apis-arnaud-lauret.pdf")
    print(pdf_parser.get_text_from(62))

    pdf_parser.close()

if __name__ == "__main__":
    main()
