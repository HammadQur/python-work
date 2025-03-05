# Assigning the messy text to a variable
messy_text = " Python programming is a fun! "

# Remove all the extra spaces at the beginning and end
cleaned_text = messy_text.strip()
print("Text after removing spaces:", cleaned_text)

# Replace "fun" with "amazing"
replaced_text = cleaned_text.replace("fun", "amazing")
print("Text after replacement:", replaced_text)

# Count how many times the letter 'i' appears
i_count = cleaned_text.count('i')
print("The letter 'i' appears", i_count, "times.")


(''' Explanation:
- `strip()` removes the leading and trailing spaces from the string.
- `replace("fun", "amazing")` replaces the word "fun" with "amazing".
- `count('i')` counts how many times the letter 'i' appears in the string.

Let me know if you'd like more details!''')