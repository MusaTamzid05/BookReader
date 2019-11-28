from book_reader import Reader

def main():

    reader = Reader(path = "/home/musa/Downloads/design-web-apis-arnaud-lauret.pdf")
    reader.read_from(62)

if __name__ == "__main__":
    main()
