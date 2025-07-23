from stats import count_words, count_characters, sorted_letter_counts

book_path = "books/frankenstein.txt"

def report(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        num_chars = count_characters(file_contents)
        sorted_list = sorted_letter_counts(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for letter in sorted_list:
            character = letter["char"]
            count = letter["num"]
            if character.isalpha() == True:
                print(f"{character}: {count}")
        print("============= END ===============")

def main():
    report(book_path)

main()