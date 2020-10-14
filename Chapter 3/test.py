mass = int(input('What is the mass of your object in kg? '))
weight = mass * 9.8

if weight > 500:
    print(weight, "Newtons. Your object is too heavy.")
elif weight > 200 and weight < 400:
    print(weight, "Newtons. Your object is perfect.")
elif weight < 100:
    print(weight, "Newtons. Your object is too light.")
else:
    print(weight, "Newtons. We are indifferent to the weight of your object.")
