# bank.py
# program that adds 2 inputted money values
# Author Daniel Finnerty

print("-Welcome to Python Bank-")
print()

amount1 = int(input("Please enter amount 1 (in cents): "))
amount2 = int(input("Please enter amount 2 (in cents): "))
total = (amount1 + amount2) / 100
print()

print (f"The total value is €{total:.2f}")