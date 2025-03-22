# read a file, count vowels, and digits in the file.
vo_count = 0
num_count = 0
try :
    file_handle = open("vowel_counter.py","r")
    #file_handle = file_handle.readlines()
    for line in file_handle:
        for char in line:
            if char.lower() in "aeiou":
                vo_count += 1
            elif char.isdigit():
                num_count += 1
except FileNotFoundError:
    print("File not found")
    quit()                  
else:
    print("vowel count:", vo_count)
    print("number count:", num_count)
    
# Compare this snippet from %23Write%20a%20Python%20program%20that%20reads%20a%20tex.py:
# #Write a Python program that reads a text file and counts the number of lines and words in it.