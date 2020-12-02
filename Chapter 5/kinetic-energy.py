# 14. Kinetic Energy
# In physics, an object that is in motion is said to have kinetic energy. The following formula can
# be used to determine a moving object’s kinetic energy:
# KE=12mv2
# The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass in
# kilograms, and v is the object’s velocity in meters per second.
# Write a function named kinetic_energy that accepts an object’s mass (in kilograms) and
# velocity (in meters per second) as arguments. The function should return the amount of kinetic
# energy that the object has. Write a program that asks the user to enter values for mass and
# velocity, then calls the kinetic_energy function to get the object’s kinetic energy

mass = int(input("What is the mass of the object in kg? "))
velocity = int(input("What is the velocity of the object in m/s? "))


def main():
    kinetic_energy(mass, velocity)


def kinetic_energy(mass, velocity):
    kineticEnergy = (mass / 2) * (velocity ** 2)
    print(kineticEnergy)


main()
