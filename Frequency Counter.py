# Frequency Counter:
# Write a program to count the frequency of each character in a string and return a dictionary (or map) with 
# characters as keys and counts as values.
# For example, given the string "hello", the output should be {'h': 1, 'e': 1, 'l': 2, 'o': 1}
s = input("Enter a string: ")
def frequency_counter(s):
    freq = {}   # empty dictionary
    for c in s: # c is a character in the string s
        if c in freq:  # if the character is already in the dictionary
            freq[c] += 1
        elif c == " ": # to ignore spaces
            continue # continue to the next character
        else:
            freq[c] = 1 # if the character is not in the dictionary, add it with a count of 1
    return freq # return the dictionary
print(frequency_counter(s)) # print the dictionary
# Time complexity: O(n) where n is the length of the string s


