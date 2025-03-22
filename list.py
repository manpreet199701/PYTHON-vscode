#print if any number in the list of input list is odd, even or prime
def check_num():
    list_num = list(map(int, input("enter the list of numbers: ").split()))
    print("the list of numbers:", list_num)
    for i in list_num:
        if i % 2 == 0:
            print(i, "is even")
        elif i % 2 != 0:
            print(i, "is odd")
        else:
            print(i, "is prime")
check_num()







