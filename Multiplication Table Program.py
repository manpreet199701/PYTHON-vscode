# Multiplication Table Program

# Ask the user for a number
num = int(input("Enter a number: "))

# Print the multiplication table from 1 to 10
print(f"Multiplication table for {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
