def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fahrenheit = float(input ("Enter the temperature in Fahrenheit: "))
fahrenheit_to_celsius(fahrenheit)
print("the value in celsius:",fahrenheit_to_celsius(fahrenheit))