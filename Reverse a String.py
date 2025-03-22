#Reverse a String:
#Write a function that takes a string as input and returns it reversed.
#Example: Input: "hello" → Output: "olleh"

#Function to reverse a string
def reverse_strings(s):
    return s[::-1]
s = input("Enter a string: ")
print("the reversed string:",reverse_strings(s))
#Test the function
