# Substring Replacement:
# Given a string and two substrings (target and replacement), replace every occurrence of the target substring with the replacement.
# Example: Replace "cat" with "dog" in "the cat sat on the catmat".
# Output: "the dog sat on the dogmat".
def substring_replacement(s, target, replacement):
    return s.replace(target, replacement)   
target = "cat"
replacement = "dog"
s = input("Enter a string: ")
if target not in s:
    print("The target substring is not in the string")
else:
    print("The replaced string is: ", substring_replacement(s, target, replacement))
#dddd