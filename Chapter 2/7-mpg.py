# Miles-per-Gallon
# A car's miles-per-gallon(MPG) can be calculated with the following formula:
# MPG = Miles driven÷Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas used. It
# should calculate the car's MPG and display the result.

milesDriven = float(input('How many miles did you drive? '))
gallonsOfGas = float(input('How many gallons gas did you use? '))

mpg = milesDriven / gallonsOfGas

print("Miles per gallon:", mpg)
