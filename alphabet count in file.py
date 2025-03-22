# read a file, count alphabet, space, and digits in the file. 
alpha_count=0
numb_count=0
space=0
try:
    file_handle=open("def attempts.py","r")
    for line in file_handle:
        for char in line:
            if char.isalpha():
                alpha_count+=1
            elif char.isdigit():
                numb_count+=1
            elif char.isspace():
                space+=1                        
    print("Number of alphabets in the file:",alpha_count)
    print("Number of digits in the file:",numb_count)
    print("Number of spaces in the file:",space)
except FileNotFoundError:
    print("File not found")
    quit()