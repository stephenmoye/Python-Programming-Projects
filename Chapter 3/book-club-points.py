# Book Club Points
# Serendipity booksPurchasedellers has a book club that awards points to its customers based on the
# number of booksPurchased purchased each month. The points are awarded as follows:
# If a customer purchases 0 booksPurchased, he or she earns 0 points.
# If a customer purchases 2 booksPurchased, he or she earns 5 points.
# If a customer purchases 4 booksPurchased, he or she earns 15 points.
# If a customer purchases 6 booksPurchased, he or she earns 30 points.
# If a customer purchases 8 or more booksPurchased, he or she earns 60 points.
# Write a program that asks the user to enter the number of booksPurchased that he or she has purchased
# this month, then displays the number of points awarded.

booksPurchased = int(
    input("How many books did you purchase this month? "))

if booksPurchased < 2:
    print("You purchased", booksPurchased, "books, and earned 0 points.")
elif booksPurchased >= 2 and booksPurchased < 4:
    print("You purchased", booksPurchased, "books, and earned 5 points.")
elif booksPurchased >= 4 and booksPurchased < 6:
    print("You purchased", booksPurchased, "books, and earned 15 points.")
elif booksPurchased >= 6 and booksPurchased < 8:
    print("You purchased", booksPurchased, "books, and earned 30 points.")
else:
    print("You purchased", booksPurchased, "books, and earned 60 points.")
