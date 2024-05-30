def is_anagram(word1:str, word2:str):
    """Checks if the two given words are anagram.

    Args:
        word1 (str): First word
        word2 (str): Second word

    Returns:
        bool: True if the two words are anagram; False if they aren't anagram.
    """
    anagram = False # Control variable
    if word1 == word2:
        return False
    else:
        for letter in word1:
            if letter in word2:
                anagram = True
            else:
                anagram = False
    return anagram


print("Is it an anagram?\nIntroduce two words to check if they are anagrams.\n\n")

word1 = input("Type the first word: ").lower()
word2 = input("Type the second word: ").lower()

print("\nPlease provide alphabetic words (only letters)")