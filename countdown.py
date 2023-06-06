""" This program counts down from a specified minute
by delaying the execution 1 second using the time sleep function.

The program raises an exception if the entered number is floating-point or less than or equal to 0"""

# Import the time library
import time

# Ask for an input from the user
n = int(input("Please, enter a positive integer to start counting down with: "))


# Raising an exception if the entered number is floating-point or less than or equal to 0
if n <= 0 or not type(n) is int:
    raise Exception("Sorry, no floating points or numbers less than or equal to zero")


# This function counts down from a given positive number
def countdown(n):
    if n == 0:
        print('Done!') # Pirint done when counting down is over
    else:
        print(n) # Print the current number
        time.sleep(1) # Pause the execution for 1 second
        countdown(n-1) # Calling the function to itself recursively


# Call the countdown function
countdown(n)

