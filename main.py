import sys
from stats import number_of_words
from stats import characters_count
from stats import sort_func

def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path) as f:
        book_content = f.read()
    return book_content

def main():
    characters_count_dict = characters_count(get_book_text)
    sorted_chars = sort_func(characters_count_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    number_of_words(get_book_text)
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
