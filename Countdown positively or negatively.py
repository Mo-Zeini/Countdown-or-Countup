""" This program counts down or up from a specified minute
according to the entered value.

It also delays the execution 1 second using the time sleep function"""

import time # Import the time library

# Ask for an input from the user
num = int(input('Enter a number: '))

""" This function expects a positive argument and counts "down"
from that number to negative one, then prints Done!"""
def countdown(n):
    if n == 0:
        print('Done!')
    else:
        print(n) # Print the current number
        time.sleep(1) # Pause the execution for 1 second
        countdown(n-1) # Calling the function to itself recursively and subtracting 1

""" This function expects a negative argument and counts "up"
from that number to positive one, then prints Done!"""
def countup(i):
    if i == 0:
        print('Done!')
    else:
        print(i) # Print the current number
        time.sleep(1) # Pause the execution for 1 second
        countup(i+1) # Calling the function to itself recursively and adding 1

""" This program decides which function to call"""
if num <= 0:
    countup(num) # Call the countup function

else:
    countdown(num) # Call the countdown function

