#Sum of Numbers (1 to n):
n = int(input("Enter a number: "))
def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1,10):
            sum += i
    return sum
print(sum_of_numbers(n))
