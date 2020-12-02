# 12. Maximum of Two Values
# Write a function named max that accepts two integer values as arguments and returns the value
# that is the greater of the two. For example, if 7 and 12 are passed as arguments to the function,
# the function should return 12. Use the function in a program that prompts the user to enter two
# integer values. The program should display the value that is the greater of the two.

def max():
    value1 = int(input("Enter your first value: "))
    value2 = int(input("Enter your second value: "))
    if value1 > value2:
        print(value1, "is greater")
    elif value2 > value1:
        print(value2, "is greater")

max()
