# Larger Than n
# In a program, write a function that accepts two arguments: a list, and a number n. Assume that
# the list contains numbers. The function should display all of the numbers in the list that are
# greater than the number n.


import random


def main():
    numList = []
    n = random.randint(0, 100)
    for num in range(10):
        randNum = random.randint(0, 100)
        numList.append(randNum)

    largerThanN(n, numList)


def largerThanN(n, numList):
    larger = []
    # print(n, numList, larger)
    for i in range(10):
        if numList[i] > n:
            larger.append(numList[i])

    print("Number n:", n)
    print("Original list:", numList)
    print("Larger than n:", larger)


main()
