# Question: Write a Python program that creates a text file named greeting.txt and writes the string "Hello, World!" into it. Then, open the file in read mode and print its contents to the console.
# Hint: Use Python’s built-in open() function with appropriate modes ('w' for writing and 'r' for reading).
file_handle= open('greeting.txt','w')
file_handle.write("Hello, World!")
file_handle.close()
file_handle= open('greeting.txt','r')
print(file_handle.read())
file_handle.close()
