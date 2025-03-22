#Find the Largest Number in a List
numbers = [3, 7, 2, 8, 4, 10]  # Step 1: Define the list
largest = numbers[0]  # Step 2: Assume the first number is the largest

for num in numbers:  # Step 3: Loop through each number in the list
    if num > largest:  # Step 4: Check if the current number is greater than 'largest'
        largest = num  # Step 5: If true, update 'largest'

print(f"Largest number: {largest}")  # Step 6: Print the final largest number