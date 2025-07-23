from stats import count_words
from stats import count_characters

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    num_words = count_words(file_contents)
    num_chars = count_characters(file_contents)
    print(f"{num_words} words found in the document")
    print(num_chars)