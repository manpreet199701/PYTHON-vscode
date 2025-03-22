import random

while True:
    program_choice = random.choice(['heads', 'tails'])
    guess = input("Guess heads or tails (or type 'exit' to quit): ").lower()
    
    if guess == 'exit':
        print("Thanks for playing!")
        break
    
    if guess == program_choice:
        print("You win!")
    else:
        print("You lose!")
#elseee





