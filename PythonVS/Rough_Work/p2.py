word = "aeroplane"

# split the string into words
words = word.split()

# create an empty dictionary to store the word counts
word_counts = {}

# loop through each word in the list
for w in words:
    # if the word is already in the dictionary, increment its count
    if w in word_counts:
        word_counts[w] += 1
    # otherwise, add the word to the dictionary with a count of 1
    else:
        word_counts[w] = 1

# loop through the dictionary and print any words that appear more than once
for w, count in word_counts.items():
    if count > 1:
        print(f"{w}: {count}")
