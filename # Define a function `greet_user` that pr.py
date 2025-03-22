# Define a function `greet_user` that prints a greeting message.
# The function should have two parameters: `name` and an optional `greeting` with a default value of `"Hello"`.
#- Call the function once with only the name.
#- Call the function again with a custom greeting (e.g., `"Hi"`).
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    name = "John"
    greeting = "Hi"
    print(f"{greeting}, {name}!")
