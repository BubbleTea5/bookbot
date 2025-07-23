def get_text(path):
    with open(path) as f:
        return f.read()

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

# provides a "key" to the .sort() function, now the .sort() knows to sort the values by the "num" key in item_list 
def sorted(item_list):
    return item_list["num"]

# takes in a dictionary with a certain letter ("char") being the *key* and number of appearances ("num") as *value*
def sorted_letter_counts(dictionary):
    letter_dicts = []
    for entry in dictionary:
        # adds {"char": *key*, "num": *value*} to letter_dicts
        letter_dicts.append({"char": entry, "num": dictionary[entry]})
    # sort() function, reverse=True means reverse order, key=sorted means it is sorting based off the sorted() function (sorting by "num" value) above
    letter_dicts.sort(reverse=True, key=sorted)
    return letter_dicts

