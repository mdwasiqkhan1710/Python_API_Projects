# Indexing

# Indexing using positive numbers
text = "Python"

first_letter_positive = text[0]
last_letter_positive = text[5]

print("First letter using positive indexing:", first_letter_positive)
print("Last letter using positive indexing:", last_letter_positive)
print() # Just for printing blank line

# Indexing using negative numbers, i.e. reverse indexing
first_letter_negative = text[-6]
last_letter_negative = text[-1]

print("First letter using negative indexing:", first_letter_negative)
print("Last letter using negative indexing:", last_letter_negative)
print() # Just for printing blank line

# Slicing
name = "Mohammad"

first_five_letters = name[0:5]
print("Slicing the text & obtaining first five letters: ", first_five_letters)

#name[start:end:step] 
# step will help in skipping the letters
skipped_letters = name[0:6:2]

print("Skipped letters: ", skipped_letters)
