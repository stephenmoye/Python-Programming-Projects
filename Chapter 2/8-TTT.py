# Tip, Tax, and Total
# Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, then calculate the amounts of a 18
# percent tip and 7 percent sales tax. Display each of these amounts and the total.

mealPrice = float(input('What is the price of your meal? '))

tip = mealPrice * .18
salesTax = mealPrice * .07
total = mealPrice + tip + salesTax

print("Amount tipped:", tip)
print("Sales tax: ", salesTax)
print("Grand total: ", total)
