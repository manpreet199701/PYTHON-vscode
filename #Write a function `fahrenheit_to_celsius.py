#Write a function `fahrenheit_to_celsius` that converts a temperature from Fahrenheit to Celsius using the formula:
#Celsius=(Fahrenheit−32)×59
#The function should take one parameter, `fahrenheit`, perform the conversion, and return the Celsius temperature.
#Use this function to convert 98.6°F to Celsius and display the result.
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
fahrenheit = float(input ("Enter the temperature in Fahrenheit: "))
fahrenheit_to_celsius(fahrenheit)
print("the value in celsius:",fahrenheit_to_celsius(fahrenheit))