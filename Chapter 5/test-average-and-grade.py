# 15. Test Average and Grade
# Write a program that asks the user to enter five test scores. The program should display a letter
# grade for each score and the average test score. Write the following functions in the program:
# calc_average. This function should accept five test scores as arguments and return the
# average of the scores.
# determine_grade. This function should accept a test score as an argument and return a
# letter grade for the score based on the following grading scale:
# Score Letter Grade
# 90–100 A
# 80–89 B
# 70–79 C
# 60–69 D
# Below 60 F

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
