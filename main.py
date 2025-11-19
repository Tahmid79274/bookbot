# from stats import get_sorted_report, get_letter_counts
# import sys

# def main():
#     if len(sys.argv) != 2:
#         print(sys.argv)
#         print("Usage: python3 main.py <path_to_book>")
#         sys.exit(1)
    
#     book_path = sys.argv[1]
#     # print(sys.argv)
#     get_sorted_report(get_letter_counts(book_path),book_path)

# main()

import sys
from stats import num_words, letter_count_dic,sorted_report

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    # print(sys.argv)
    # Prints ['main.py', 'books/frankenstein.txt']

    # print(sys.argv[0])
    # Prints 'main.py'

    # print(sys.argv[1])
    # Prints 'books/frankenstein.txt'
    if len(sys.argv) != 2:
        # print(sys.argv)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    content = get_book_text(sys.argv[1])
    print(f"Found {num_words(content)} total words")
    letter_count = letter_count_dic(content.lower())
    sorted_list = sorted_report(letter_count)
    
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
# get_book_text
main()