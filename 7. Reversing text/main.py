TEXT = "Hello World"

# With for loop
reversed_word = ""

for letter in TEXT:
    reversed_word = letter + reversed_word
    
print(reversed_word)

# With slicing
reversed_word2 = TEXT[::-1]

print(reversed_word2)