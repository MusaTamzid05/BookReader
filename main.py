from book_reader.speaker import speak
from book_reader.parser import PDFParser

def main():
    #speak("This is a message.")

    pdf_parser = PDFParser(path = "/home/musa/Downloads/webassembly-action-eexamples-emscripten.pdf")


if __name__ == "__main__":
    main()
