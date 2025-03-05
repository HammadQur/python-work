# Assigning the sentence to a variable
sentence = "The quick brown fox jumps over the lazy dog"

# Split the sentence into a list of words
words_list = sentence.split()
print("List of words:", words_list)

# Join the words back together with dashes between them
joined_sentence = '-'.join(words_list)
print("Sentence with dashes:", joined_sentence)

# Check if the sentence starts with "The"
starts_with_the = sentence.startswith("The")
print("Does the sentence start with 'The'? ", starts_with_the)

# Find the position of the word "fox"
position_of_fox = sentence.find("fox")
print("The position of the word 'fox':", position_of_fox)


('''Explanation:
- `split()` splits the sentence into a list of words based on spaces.
- `'-'.join()` joins the words back together, but places a dash (`-`) between each word.
- `startswith("The")` checks if the sentence starts with the specified string.
- `find("fox")` returns the index of the first occurrence of the word "fox" in the sentence (if found), or `-1` if it's not found.''')

