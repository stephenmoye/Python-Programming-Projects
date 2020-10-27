# Celsius to Fahrenheit Table
# Write a program that displays a table of the Celsius temperatures 0 through 20 and their
# Fahrenheit equivalents. The formula for converting a temperature from Celsius to Fahrenheit is
# F=95C+32
# where F is the Fahrenheit temperature, and C is the Celsius temperature. Your program must
# use a loop to display the table

print('Celsius | Fahrenheit')
print('--------------------')

for degC in range(0, 21):
    degF = (degC * (9/5) + 32)
    print(degC, '\t', degF)
