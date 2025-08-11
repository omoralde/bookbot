def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"{text} words found in the document")


def get_book_text(path):
    with open(path) as f:
        fulltext = f.read()
        wordcount = len(fulltext.split())
        return wordcount

main()

