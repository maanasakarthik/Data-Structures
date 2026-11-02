# First and Last character of words match
def match_words(words):
    count = 0 
    list = []
    for word in words:
        if len(word) > 1 and word [0] == word[-1]:
            count += 1
            list.append(word) # Adds matching word to the list 
            # insert() allows to place an element at a specific index (position) in the list.

    print("List of words with first and last character as the same \n", list)
    return count

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221' ])
print("Number of words having first and last character as the same: ", count)