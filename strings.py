#Strings
# Beginner:Write a program that prompts the user for a string and prints the number of characters in the string (excluding spaces).
#Intermediate: Write a Python program that takes a sentence as input and prints all unique characters (ignoring case) along with their frequency count.
#Advanced:Write a Python program that extracts all email addresses from a given multi-line string using regular expressions. Print the list of extracted email addresses.
in_string = input("Enter a string: ")
count=0
for i in in_string:
    if i != ' ':
        count+=1
print(count)    
