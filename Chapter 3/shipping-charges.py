# Shipping Charges
# The Fast Freight Shipping Company charges the following rates:
# Weight of Package Rate per Pound
# 2 pounds or less $1.50
# Over 2 pounds but not more than 6 pounds $3.00
# Over 6 pounds but not more than 10 pounds $4.00
# Over 10 pounds $4.75
# Write a program that asks the user to enter the weight of a package then displays the shipping
# charges.

weight = float(input('What is the weight of your object in lbs? '))

if weight <= 2:
    print(weight, "lbs costs $1.50")
elif weight > 2 and weight <= 6:
    print(weight, "lbs costs $3.00")
elif weight > 6 and weight <= 10:
    print(weight, "lbs costs $4.00")
else:
    print(weight, "lbs costs $4.75")
