# Rainfall Statistics
# Design a program that lets the user enter the total rainfall for each of 12 months into a list. The
# program should calculate and display the total rainfall for the year, the average monthly rainfall,
# the months with the highest and lowest amounts.

rainData = []


def main():
    for month in range(1, 13):
        print("Enter the total rainfall for month (inches)", month, ":")
        rain = int(input())
        rainData.append(rain)

    average(rainData)


def average(rainData):
    total = 0

    for data in range(0, 12):
        total = total + rainData[data]

    average = total / 12

    print("Total rainfall:", total, "inches")
    print("Average rainfall:", average)
    print("Lowest rainfall:", min(rainData))
    print("Highest rainfall:", max(rainData))


main()
