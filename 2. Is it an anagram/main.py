print("Is it an anagram?\nIntroduce two words to check if they are anagrams.\n\n")
word1 = input("Type the first word: ").lower()
word2 = input("Type the second word: ").lower()

anagram = False
if word1 == word2:
    print("Words are the same")
else:
    for letter in word1:
        if letter in word2:
            anagram = True
        else:
            anagram = False
print(anagram)