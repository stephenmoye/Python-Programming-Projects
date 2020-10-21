# Magic Dates
# The date June 10, 1960, is special because when it is written in the following format, the month
# times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit
# year. The program should then determine whether the month times the day equals the year. If
# so, it should display a message saying the date is magic. Otherwise, it should display a message
# saying the date is not magic.

print("~*Magic Date Detector*~")
print("Please input all dates in 2 digit number form MM/DD/YY")

month = int(input("What is the month? "))
day = int(input("What is the day? "))
year = int(input("What is the year? "))

if month * day == year:
    print(month, "/", day, "/", year, "is a Magic Date!")
else:
    print(month, "/", day, "/", year, "is NOT a Magic Date. :(")
