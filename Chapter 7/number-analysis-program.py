# Number Analysis Program
# Design a program that asks the user to enter a series of 20 numbers. The program should store
# the numbers in a list then display the following data:
# The lowest number in the list
# The highest number in the list
# The total of the numbers in the list
# The average of the numbers in the list


numbersList = []


def main():
    for month in range(0, 20):
        print("Enter any number")
        numbers = int(input())
        numbersList.append(numbers)

    analyze(numbersList)


def analyze(numbers):
    total = 0

    for nums in range(0, 20):
        total = total + numbers[nums]

    average = total / 20

    print("Lowest number:", min(numbers))
    print("Highest number:", max(numbers))
    print("Total:", total)
    print("Average:", average)


main()
