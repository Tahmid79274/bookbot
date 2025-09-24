from stats import get_sorted_report, get_letter_counts
import sys

def main():
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    # print(sys.argv)
    get_sorted_report(get_letter_counts(book_path),book_path)

main()