def main():
    book_path = "books/frankenstein.txt"
    from stats import get_num_words
    from stats import get_num_chars
    from stats import get_sorted_dict
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    freq = get_num_chars(text)
    sorted = get_sorted_dict(freq)
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ----------")
    for each in sorted:
        print(each)
    print("=========== END ==========")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
