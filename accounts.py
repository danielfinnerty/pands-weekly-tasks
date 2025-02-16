# accounts.py
# program that reads a 10 character account number and outputs showing only the last 4
# Author Daniel Finnerty

'''
account = input("Please enter a 10 digit account number: ")
x = len(account)

if x != 10: print("Incorrect number of digits. Please try again")
elif x == 10: print("XXXXXX" + account[6:])
'''

# Extra task - Unlimited Account Number Length


account = input("Please enter your account number: ")
x = len(account)

print(((x - 4) * "X") + account[(x - 4):])