# es.py
# program that counts the number
# of e's from a text file
# Author: Daniel Finnerty

# Python program to demonstrate sys.argv
#source = https://www.geeksforgeeks.org/command-line-arguments-in-python/

import sys
import os.path

if len(sys.argv) == 1: # number of arguements needs to exceed 1 (script name)
    print("Filename not entered. Please try again")

elif len(sys.argv) > 1:
    FILENAME = (sys.argv[1])
    
    if (FILENAME[-3:] != "txt"): # confirming file is 'txt'
        print("File entered is not a text file. Please try again")
    
    elif not os.path.isfile(FILENAME): # confirming if file is found
        print ("File does not exist. Please check and try again.")
    
    elif os.path.isfile(FILENAME): #count number of e's
        def readNumber ():
            with open (FILENAME) as f:
                number = f.read()
                return number
        num = readNumber()
        amount = num.count("e")
        print(amount)