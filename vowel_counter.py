# Count Vowels and Consonants:
# Write a function that counts the number of vowels and consonants in a string.
# Example: "programming" → Vowels: 3, Consonants: 8
words = input("Enter a word: ")
def count_vowels(words):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    v = 0
    c = 0
    for i in words:
        if i in vowels:
            v += 1
        elif i in consonants:
            c += 1
    return f"Vowels: {v}, Consonants: {c}"
print(count_vowels(words))
# Output: