## Programming Project 8
## Payroll Program (Input Validation)

## Defining the main function to call calculateGrossPay
def main():
    ## Calling the get pay, get hours worked, and calculate gross pay function
    getPay()
    getHoursWorked()
    calculateGrossPay()

## Getting the users pay rate for validation
def getPay():
    ## Storing constants for limitations for the pay rate
    MINIMUMPAY = float(7.5)
    MAXIMUMPAY = float(18.25)

    ## Storing the users pay rate input
    ## Declaring the global variable
    global pay
    pay = input("Please enter your pay rate per hour: $")

    ## Checking the users input to make sure its a number
    ## In case the user input is not a digit
    while not pay.replace(".", "", 1).isdigit():
        print("ERROR: Invalid Input. Please only use digits.")
        pay = input("Please enter a valid amount of pay: $")
        
    ## Comparing the pay input with the minimun and maximum pay rates
    ## In case the user input is not between $7.50 and $18.25
    while float(pay) < MINIMUMPAY or float(pay) > MAXIMUMPAY:
        ## Informing the user they've entered something out of the limitations
        print("ERROR: Pay Rate must be between $7.50 to $18.25")
        pay = input("Please enter a valid amount of pay: $")
        
## Getting the users hours worked for validation
def getHoursWorked():
    ## Storing constants for limitations for the hours worked
    MINIMUMHOURS = int(1)
    MAXIMUMHOURS = int(40)

    ## Storing the users hours worked
    ## Declaring the global variable
    global hours
    hours = input("Please enter how many hours you've worked:")

    ## Checking the users input to make sure its a number
    ## In case the user input is not a digit
    while not hours.replace(".", "", 1).isdigit():
        print("ERROR: Invalid Input. Please only use digits.")
        hours = input("Please enter a valid amount of hours: ")
        
    ## Checking to see if the users input is between 1 and 40 hours
    ## In case the user input is not between 1 and 40
    while float(hours) < MINIMUMHOURS or float(hours) > MAXIMUMHOURS:
        ## Informing the user they've entered something out of the limitations
        print("ERROR: Hours worked must be between 1 to 40 hours")
        hours = input("Please enter a valid amount of hours: ")

## Calculating the user's inputs to display their gross pay
def calculateGrossPay():
    ## Declaring the global variables
    global pay
    global hours 
    ## Calculating the gross pay total and storing it as a variable
    grossPay = float(pay) * float(hours)

    ## Displaying the gross pay
    print(f"Here's your gross pay: ${grossPay:,.2f}")
    ## Calling the retry function
    retry()

## Asking user to redo another calculation         
def retry():
    ## Getting users input for answer
    answer = input("Would you like to do another calculation? Enter ""Y"" or ""N"": ")
    
    ## Checking to see if user entered a letter
    ## In case the user input is not a character
    while not answer.isalpha():
        print("ERROR: Invalid Input. Please only use letters.")
        retry()

    ## Checking to see if user entered only Y or N
    ## If user enters "y"
    if answer.lower() == "y":
        ## By calling main it calls all prior functions to trigger a loop
        main()
    ## If user enters "n"
    elif answer.lower() == "n":
        print("Thank you for your time today! Goodbye!")
    ## If user enter any other letter
    else:
        print("ERROR: Invalid Input. Please only use ""Y or ""N""")
        ## Calling the retry function to ask them again
        retry()
    ## End If

## Calling main function 
main()


## Reflection
"""
I've started writing this program a few weeks back prior to me reaching
chapter 7 in our textbook. Originally I wrote majority of my code in
just one function. It worked, however certain responses would trigger
at unwanted times or certain responses didn't trigger when supposed to.
I went and repeatedly tried to separate the necessary steps and break
them down into functions. After constant errors with the responses, I
went back and rewrote some code, almost turning all my functions into 
value-returning functions. Tried a few of methods and the program worked,
however, the variables when asked again after validation, was not being
saved in order to do the calculations with, and it instead was doing the 
calculations with the previously stated input despite the error it triggered.
I literally gave myself a 3 week headstart on this program, I've worked 
with classmates all day and between the hours of 9:30pm and 10:30pm of 
Nov 19th, my brain had the bright idea to declare the needed variables 
for the gross pay calculations as "global" variables. After trying that, 
the program worked successfully, alot of the unwanted responses stopped, 
and I was able to achieve my desired results. 
"""