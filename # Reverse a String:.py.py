# Reverse a String:
# Write a function that takes a string as input and returns it reversed.
# Example: Input: "hello" → Output: "olleh"
def reverse_string(s):
    # s[::-1] creates a new string with the characters in reverse order.
    return s[::-1]
input_str = input("Enter a string: ")
print("Input:", input_str)
print("Output:", reverse_string(input_str))
