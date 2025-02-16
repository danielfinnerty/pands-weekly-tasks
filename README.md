# Programming and Scripting Weekly Tasks

by: Daniel Finnerty

## Weekly Task 02

Creation of program called bank.py which adds 2 amounts entered by the user, and prints out the answer in readable euro and cent format.

### Comments

Once I understood to specify the inputs as integers, the code was easy to create. I did however, notice an issue when the final figure would end with a zero as it wouldn't be display (€2.5 rather than €2.50). I did find the solution on the below link, and was able to specify the total value be displayed with 2 decimal places at all times.

https://www.w3schools.com/python/python_string_formatting.asp

Finally, to make the output more legible, I added empty lines using print()

## Weekly Task 03

Creat a Python program called accounts.py which requests a 10 digit account number, then displays it but only showing the final 4 digits.

### Comments

This is broken down into 2 sections:
    1. Ensure the number entered has 10 digits
    2. If correct, return the entered number but only displaying the final 4 characters.

For the first task, I confirmed what I needed in the below link. Using len() counted the number of characters entered by the user.

https://www.w3schools.com/python/ref_func_len.asp#:~:text=The%20len()%20function%20returns,of%20characters%20in%20the%20string.

This was then followed by the below link showng elif command. Using this allowed conditions whereby if 10 digits were not entered, the code would request to try again, but if the account number was correct, it would output the last 4 digits.

https://www.w3schools.com/python/python_conditions.asp

### Extra Task

To modify the program so it can handle account numbers of any length, I did have to remove the conditions however, I still utilised the len() command to count the number of digits. Given the number inputted could be of any length, I factored this into the formula and using 'x' as the quantity of characters in the account numnber, the number of 'X's to print in the result would therefore be 'x-4'. Simialr could be used to specify the last 4 digits to display clearly, starting at the 4th last digit, or again 'x-4'.

# End