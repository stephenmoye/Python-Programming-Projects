# Celsius to Fahrenheit Temperature Converter
# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is
# as follows:
# F = 95C+32
# The program should ask the user to enter a temperature in Celsius, then display the temperature
# converted to Fahrenheit.

tempC = float(input("Enter the temperature in Celsius "))
tempF = (tempC * 9/5) + 32

# end= allows the characters in the ' ' to be added to the end of the output, without the space
print(tempC, end='C equals ')
print(tempF, end='F')
