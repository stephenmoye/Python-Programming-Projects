# Lottery Number Generator
# Design a program that generates a seven-digit lottery number. The program should generate
# seven random numbers, each in the range of 0 through 9, and assign each number to a list
# element. (Random numbers were discussed in Chapter 5.) Then write another loop that displays
# the contents of the list.


import random

ticket = []

for num in range(0, 7):
    randNum = random.randint(0, 9)
    ticket.append(randNum)

print("Your lottery numbers are:")
print(ticket)
