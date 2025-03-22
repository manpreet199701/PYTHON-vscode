#odd even checker
num1 = float(input("ENTER THE VALUE-"))
num2 = float(input("ENTER THE VALUE-"))
#odd even checker
def odd_even_checker(num1,num2):
    if num1 % 2 == 0:
        print("the number is even-")
    elif 2 % num1 != 0:
        print("th number is odd-")
    else:
        print("wrong number")
    if num2 % 2 == 0:
        print("the number is even-")
    elif 2 % num2 != 0: 
        print("the number is odd-")
    else:
        print("wrong number")
#calling the function   
odd_even_checker(num1,num2)
#end of the program
#output
#ENTER THE VALUE-3
#ENTER THE VALUE-4          
        


