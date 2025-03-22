# Prompt the user for a positive integer n and use a while loop to calculate and print the sum of numbers from 1 to n.
# If the user enters a negative number, print an error message and prompt the user again.
# If the user enters 0, exit the program.
def pos_int(number):
    i =1
    sum= 0
    while i <= number:
        sum += i
        i += 1
    return sum  # return the sum of numbers from 1 to n
    if number < 0:
        print("Error: Please enter a positive number")
    elif number == 0:
        print("Exiting the program")
        exit()
print (pos_int(5)) # 15

