# 13. Falling Distance
# When an object is falling because of gravity, the following formula can be used to determine the
# distance the object falls in a specific time period:
# d=12gt2
# The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the
# amount of time, in seconds, that the object has been falling.
# Write a function named falling_distance that accepts an object’s falling time (in seconds) as
# an argument. The function should return the distance, in meters, that the object has fallen during
# that time interval. Write a program that calls the function in a loop that passes the values 1
# through 10 as arguments and displays the return value.



def falling_distance():
  



  score = 0
total = 0


def calc_average(score, total):
    for tests in range(5):
        score = int(input("What is the score of test?"))
        total += score
    average = total / 5
    return letter_grade(average)


def letter_grade(average):
    if average > 90:
        grade = "A"
    elif average > 80:
        grade = "B"
    elif average > 70:
        grade = "C"
    elif average > 60:
        grade = "D"
    else:
        grade = "F"

    print("Your average score of", average, "equals", grade)


calc_average(score, total)

