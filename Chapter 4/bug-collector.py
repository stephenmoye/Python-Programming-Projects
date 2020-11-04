# The Bug Collector Problem
# A bug collector collects bugs every day for five days. Write a program that keeps a running total
# of the number of bugs collected during the five days. The loop should ask for the number of
# bugs collected for each day, and when the loop is finished, the program should display the total
# number of bugs collected.


bugs = 0
day = 0

while day < 5:
  bugs += int(input('How many bugs did you collect today? '))
  day += 1

print('Total bugs collected: ', bugs)