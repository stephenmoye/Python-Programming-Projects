# Sales Tax
# Write a program that will ask the user to enter the amount of a purchase. The program should
# then compute the state and county sales tax. Assume the state sales tax is 5 percent and the
# county sales tax is 2.5 percent. The program should display the amount of the purchase, the
# state sales tax, the county sales tax, the total sales tax, and the total of the sale(which is the sum
# of the amount of purchase plus the total sales tax).

price = float(input('What is the price of your purchase?'))

stateTax = price * .05
countyTax = price * .025
totalTax = stateTax + countyTax
grandTotal = price + totalTax

print("State tax:", stateTax)
print("County tax: ", countyTax)
print("Total tax: ", totalTax)
print("Grand total: ", grandTotal)
