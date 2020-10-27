# Sum of Numbers
# Write a program with a loop that asks the user to enter a series of positive numbers. The user
# should enter a negative number to signal the end of the series. After all the positive numbers
# have been entered, the program should display their sum.

# ask for number
num = int(input('Please enter a number: '))
count = 0

while num >= 0:
    count += num
    num = int(input(
        'Please enter a + number to continue, or a - number to end program: '))

print("total:", count)
