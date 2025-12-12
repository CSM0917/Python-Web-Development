## Class Discussion Assignment (For Loops: Using range())

## Constant for the maximum number
MAX_VALUE = 1001

## Getting the first number of the list
num = int(input("Enter a number to start with: "))
## Getting the number to count by in the list
counter = int(input("Enter the number you'd like to count by: "))

## Beginning from the number 0, ending @ 1,000, counting based off the number stored in the variable
for num in range (num, MAX_VALUE, counter):

    ## Printing the results
    print(num)
