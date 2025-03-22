#You need to complete a program that calculates the sum of numbers from 1 to n, where n is provided by 
# the user.
number = int(input("enter the number: "))
sum = 0
for i in range(0, number + 2):
    sum += i
    print(sum)  # Output the result 