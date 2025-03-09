# squareroot.py
# Week 06 weekly task

# Program that request positive floating point number and
# outputs the approximate square root thorugh Newtons method

# Author: Daniel Finnerty


def sqrt(number):
    estrt = (1) # estimated root
    count = (0)
    while count != 100:
        estrt = 0.5 * (estrt + (number / estrt))
        count = count + 1
    return (estrt)


number = float(input("Please enter a positive number: "))
while number <= 0:
    print("Entry is not a positive number.")
    number = float(input("Please try again: ")) # Confirmation number is positive.

print (f"The square root of {number} is {sqrt(number):.1f}.")
