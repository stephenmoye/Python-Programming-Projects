# Total Purchase
# A customer in a store is purchasing five items. Write a program that asks for the price of each
# item, then displays the subtotal of the sale, the amount of sales tax, and the total. Assume the
# sales tax is 7 percent.

item1 = float(input('What is the price of your first item? '))
item2 = float(input('What is the price of your second item? '))
item3 = float(input('What is the price of your third item? '))
item4 = float(input('What is the price of your fourth item? '))
item5 = float(input('What is the price of your fifth item? '))

subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * .07
total = subtotal + tax

print("Subtotal:", subtotal)
print("Sales tax: ", tax)
print("Total: ", total)
