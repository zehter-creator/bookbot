import sys
from stats import string_accept, string_to_count, sort_on, sort_char

def get_book_text(path):
    with open(path) as f:
        return f.read()

    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    m =get_book_text(path_to_file)
    lenght = string_accept(m)
    transform= string_to_count(m)
    print("============ BOOKBOT ============ \nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {lenght} total words")
    print("--------- Character Count -------")
    for item in sort_char(transform):
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()