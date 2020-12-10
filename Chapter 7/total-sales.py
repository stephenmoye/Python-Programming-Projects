# Total Sales
# Design a program that asks the user to enter a store’s sales for each day of the week. The
# amounts should be stored in a list. Use a loop to calculate the total sales for the week and
# display the result

def sales():
    allSales = []

    for x in range(1, 8):
        print("Enter the stores sales for day", x)
        day = float(input())
        allSales.append(day)

    total(allSales)


def total(allSales):
    total = 0
    for y in range(0, 7):
        total = total + allSales[y]

    print("Total sales for the week: $", total)


sales()
