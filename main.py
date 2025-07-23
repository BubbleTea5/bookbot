import sys
from stats import get_text, count_words, count_characters, sorted_letter_counts

def main():
        # sys.argv is a list populated based on what arguments are given in the command line, anything input in the CLI after python3 would be an argument
        # so the sys.argv list if program is used properly would be [main.py, <path to book>]
        if len(sys.argv) == 1:
             print("Usage: python3 main.py <path_to_book>")
             #sys function that tells the code to exit out using a number, in this case "1" which typically represents general error
             sys.exit(1)
        # sys.argv[1] would be the path to the book, explanation in comments and if function above
        book_path = sys.argv[1]
        text = get_text(book_path)
        num_words = count_words(text)
        num_chars = count_characters(text)
        sorted_list = sorted_letter_counts(num_chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for letter in sorted_list:
            # you can use .isalpha() on the *value*
            if letter["char"].isalpha():
                print(f"{letter['char']}: {letter['num']}")
        print("============= END ===============")

main()