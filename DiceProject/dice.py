import random

min_value = 1 # the minimum value of dice
max_value = 6 # the maximum value of dice

#logic for rolling the dice again
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print(random.randint(min_value,max_value))
    roll_again = input("Would you like to roll again: ")

