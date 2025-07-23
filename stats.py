def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letter_count = {}
    for letter in text:
        # converts lettters to lowercase
        s_letter = letter.lower()
        # if the s_letter is found as a *key* in the dictionary, add 1 to the *value*
        if s_letter in letter_count:
            letter_count[s_letter] += 1
        # else, set the value as 1
        else:
            letter_count[s_letter] = 1
    return letter_count
