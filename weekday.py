# weekday.py
# Week 05 weekly task
# Program that outputs if today is a weekday or not
# Author: Daniel Finnerty


# Source for datetime: https://www.w3schools.com/python/python_datetime.asp

import datetime

fullDate = datetime.datetime.now() # gives full date and time stamp

day = fullDate.strftime("%A") # converts date and time stamp to just the day.

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day != (days[0]) and day != (days[-1]):
    print("\033[31mYes, unfortunately today is a weekday.\033[0m") # Source for colour setting: https://vascosim.medium.com/how-to-print-colored-text-in-python-52f6244e2e30
else:
    print("\033[31mIt is the weekend, yay!\033[0m")


'''
# Alternative solution below but gives the day as a number (0 - 6) instead of the actual day.

import datetime

fullDate = datetime.datetime.now()

day = int(fullDate.strftime("%w")) # converts date and time stamp to just a number (0-6 with Sunday a zero)

if day != 0 and day != 6:
    print("\033[31mYes, unfortunately today is a weekday.\033[0m")
else:
    print("\033[31mIt is the weekend, yay!\033[0m")

'''