# Software Sales
# A software company sells a package that retails for $99. Quantity discounts are given according
# to the following table:
# Quantity Discount
# 10–19 10%
# 20–49 20%
# 50–99 30%
# 100 or more 40%
# Write a program that asks the user to enter the number of quantity purchased. The program
# should then display the amount of the discount(if any) and the total amount of the purchase
# after the discount.

PACKAGE = 99
quantity = int(input("How many packages did you purchase? "))


if quantity <= 10:
    print("Less than 10 packages do not receive a discount.")
    print("Total: $", quantity * PACKAGE)
elif quantity > 10 and quantity <= 19:
    print(quantity, "packages receives a discount of 10%")
    print("Total: $", quantity * PACKAGE * .90)
elif quantity > 20 and quantity <= 49:
    print(quantity, "packages receives a discount of 20%")
    print("Total: $", quantity * PACKAGE * .80)
elif quantity > 50 and quantity <= 99:
    print(quantity, "packages receives a discount of 30%")
    print("Total: $", quantity * PACKAGE * .70)
else:
    print(quantity, "packages receives a discount of 40%")
    print("Total: $", quantity * PACKAGE * .60)
