# Read a text file and count: total characters, total words and total lines
fhand = open('ticke.py','r') # Open the file in read mode
count = 0 # Initialize line count
for character in fhand: #
    print(len(character)) # Print the length of each line
    count = count + 1
    print(count) 
print("Total number of lines in the file:", count)
fhand.close() # Close the file