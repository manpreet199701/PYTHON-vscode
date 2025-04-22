#Write a Python program to open a text file named sample.txt, read its contents, and print them to 
# the console.
#file_handle=open('Frequency Counter.py')
#count=1
#for i in file_handle:
 #   print(count, ":", i)
  #  count = count + 1
   # print(i)
#file_handle.close() 
file_handle = open('game.py')
lines=file_handle.readlines()
list(lines)
for i in lines:
    print(i)
file_handle.close()