fhand = open('game.py','r') # Open the file in read mode
count = 0 # Initialize line count
for line in fhand: #
  for letter in line :
        if letter == 'g':
            count = count + 1 # Increment line count
print("Total number of letter g in the file:", count) # Print total lines
fhand.close() # Close the file
