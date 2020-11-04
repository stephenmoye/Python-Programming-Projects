# Budget Analysis
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the month and keep
# a running total. When the loop finishes, the program should display the amount that the user is
# over or under budget.

budget = float(input('What is your budget? '))
total = 0

while total < budget:
  expense = float(input('What is the price of your purchase? '))
  total += expense

print('You are over budget!')
print('Budget:', budget)
print('Total:', total)