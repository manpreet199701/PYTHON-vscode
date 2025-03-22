#substring Replacement:
#Given a string and two substrings (target and replacement), replace every occurrence of the target substring with the replacement.
#Example: Replace "cat" with "dog" in "the cat sat on the catmat".

def substring_replacement(string, target, replacement):
    return string.replace(target, replacement)
target= "n"
replacement= "game"
string= input("Enter a string: ")
new_string= string.replace(target, replacement)
print("the original string:", string)
print("the target:", target)
print("the replacement:", replacement)  
print("the new string:", new_string)
