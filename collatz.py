# collatz.py

# Program that asks user to input a positive integer,
# and runs that number through a series of calculations,
# according to the Collatz conjecture until result is 1.

# Author Daniel Finnerty

number = int(input("Please enter a positive number: "))

while number <= 0:
    print("Number is not a positive integer.")
    number = int(input("Please try again: ")) # Confirmation integer is positive.

print(number)

while number != 1:

    if (number % 2) == 0:
        number = int(number / 2) # Sepcified resulting figure as an integer, otherwise outputs float.
        print(number)
    
    elif (number % 2) == 1:
        number = int(number * 3) + 1
        print(number)

    else:
        print(number)

    
