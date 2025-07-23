from stats import get_text, count_words, count_characters, sorted_letter_counts

def main():
        book_path = "books/frankenstein.txt"
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