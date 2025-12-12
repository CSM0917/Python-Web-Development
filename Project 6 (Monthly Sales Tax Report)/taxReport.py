## Programming Project 6
## Monthly Sales Tax Report (Modularizing Programs with Functions)
## This program will allow users to input their sales amount in exchange for being displayed their tax amounts from State and County

## Defining the main function to peform the other necessary functions
def main():
    ## Calling all functions to display and calculate the sales and tax amounts
    getSales()
    getStateTax()
    getCountyTax()
    calculateTotalTax()
    calculateTotal()

## Defining the getting users input for their sales amount function
def getSales():
    ## Globally defining the sales variable
    global sales
    ## Asking user to provide input for sales and storing them as the variable "sales"
    sales = float(input("Enter the total sales for the month: $"))
    ## Displaying sales amount entered and preparing for the displaying of the totals
    print(f"You've entered: ${sales} \nHeres your totals: ")

## Defining the state tax function
def getStateTax():
    ## Globally defining the state tax constant and storing it as 4%
    global STATETAX
    STATETAX = float(.04)
    ## Calculating the sales amount with the 4% taxes, rounding the results, then storing it under "stateTaxTotal"
    stateTaxTotal = round(sales * STATETAX, 2)
    ## Displaying the state tax amount
    print(f"State Tax: ${stateTaxTotal}")

## Defining the county tax function
def getCountyTax():
    ## Globally defining the county tax constant and storing it as 2%
    global COUNTYTAX
    COUNTYTAX = float(.02)
    ## Calculating the sales amount with the 2% taxes, rounding the results, then storing it under "countyTaxTotal"
    countyTaxTotal = round(sales * COUNTYTAX, 2)
    ## Displaying the county tax amount
    print(f"County Tax: ${countyTaxTotal}")

## Defining the total tax amount function
def calculateTotalTax():
    ## Calculating the tax amount with the state tax and county tax from the sales
    totalTax = round(sales * STATETAX + sales * COUNTYTAX, 2)
    ## Displaying the total tax amount 
    print(f"Total Tax Amount: ${totalTax}")

## Defining the total calculations function
def calculateTotal():
    ## Calculating the sales amount with the previous tax amounts
    ## Example: total = 300 + (300 * 0.02 = 6) + (300 * 0.04 = 12) = 318
    total = round(sales + sales * STATETAX + sales * COUNTYTAX, 2)
    ## Displaying the total amount added with the previously stated tax amount
    print(f"Total Sales (Taxes Included): ${total}")

main()

## Reflection Time 
"""
Originally when I began this program, I read through the first page 
of instructions, using the previous knowledge from project 5 and back, I
foolishly created the program using the While and For loops. After
further reading, I quickly realized I did the assignment incorrectly,
and proceeded to thinking of ways to incorporate what I've previously
written. For instance I've stored my constants and variable globally 
outside of a function originally, but after trial and error, I've managed
to put them in the correct funtions needed to get the desired results. 
After figuring out a way to fit the requirements, I began to struggle 
with the total calculations of the taxes with the sales. For the calculations 
I've decided to define the "sales" variable as the only global variable, and 
repeatedly used that with the addition of the state and county tax constants. 
I believe there is a way to establish being able to use the functions 
together for easier coding, but instead I just opted for ol reliable math.
It's a bit repetitive, but the program work as desired. After making sure
everything worked as needed, I thought of ways to limit as much coding 
written within the main() function, so I went back and created a function
for everything I was trying to accomplish, then called them all in main, so
main will hold just the function calls. 
"""
