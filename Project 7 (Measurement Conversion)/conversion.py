## Programming Project 7
## Tablespoon and Cup Measurement Conversion (Value Returning and Void Functions)

## Declaring global constant to use for calculations
CONVERSION_NUMBER = int(16)

## Defining the main function
def main():
    ## Calling the getUserInput() function
    getUserInput()

## Defining the getUserInput() to receive and store user input to display results
def getUserInput():
    ## Declaring the local variables and receiving the users input to store
    type = str(input("Enter the unit of measurement for you're converting (T for Tablespoons, C for Cups): "))
    num = float(input("Enter the number that you'd like to calculate: "))
        
    ## If/Else statement to compare the users measurement type input for the needed functions
    ## If user enter tablespoons, it will convert their entered amount into the cups unit of measurement
    if type == "t" or type == "T":
        tbspToCups(num)
        return getUserAnswer()
        
    ## If user enter cups, it will convert their entered amount into the tablespoons unit of measurement
    elif type == "c" or type == "C":
        cupsToTbsps(num)
        return getUserAnswer()
        
    ## If user enters anything other than "t" or "c", it will display an error message and ask the user for its input again
    else:
        print(f"You've entered an incorrect unit of measurement: {type}, please enter ""T"" or ""C"" please.")
        return getUserInput()
    
    # End If
        
## Defining the tablespoons to cups conversion function to accept and pass the amount entered 
def tbspToCups(tbspsEntered):

    ## Dividing the entered amount of tablespoons by the conversion number and Storing the result under the local variable "cups"
    cups = tbspsEntered / CONVERSION_NUMBER

    ## Display the entered amount of tablespoons and converted cups it equates to
    print(f"{tbspsEntered} tablespoons is equal to {cups} cups.")
    return cups

## Defining the cups to tablespoons conversion function to accept and pass the amount entered  
def cupsToTbsps(cupsEntered):

    ## Multiplying the entered amount of cups with the conversion number and Storing the result under the local variable "tablespoons"
    tablespoons = cupsEntered * CONVERSION_NUMBER

    ## Display the entered amount of cups and converted tablespoons it equates to
    print(f"{cupsEntered} cups is equal to {tablespoons} tablespoons.")
    return tablespoons

## Defining the getUserAnswer() function to ask the user if they'd like to run the conversion loop again
def getUserAnswer():

    ## Asking user for response to converting again and storing their response
    answer = str(input("Would you like to convert again? (Enter ""Y"" for Yes, ""N"" for No): "))

    ## If/Else statement to compare the users answer with the necessary response on whether they'd like to rerun the loop
    ## If user responds "yes", run the getUserInput function again
    if answer == "Y" or answer == "y" or answer == "yes":
        return getUserInput()
    
    ## If user responds "no", display goodbye message and end the program
    elif answer == "N" or answer == "n" or answer == "no":
        print("Goodbye, thank you for spending time with me! Just let me know when you need to another conversion!")

    ## If user doesn't enter a valid response, run the question again to get an accurate one
    else:
        print("Huh? That doesn't seem like a valid response, lets try that again!")
        return getUserAnswer()
    
## Call the main function to start program
main()

## Reflection 
"""
While creating this program, I opted out of creating a flowchart first,
and went straight into coding. After reading the requirements, I 
started thinking of ways to calculate tablespoons and cups, so I looked
up how many tablespoons was in a cup. Google informed me that its 16 tbsps
in 1 cup, so for the coversions, I saved 16 as a constant to use for the 
formulas. For tbsps, I divided the amount with the constant to give the 
results for the cups, and for the cups, I multiply the amount by the 
constant to display the amount of tablespoons it equates to. Upon further
inspection, I realized in the requirements, the last step asked to ask the
user if they'd like to convert again after the initial conversion. I began
thinking of ways to do that, so I created the getUserAnswer function. To
keep it simple, I replicated the way I did the conversion functions for main
in a similar way as I did with the answer function by using If/Else 
statements.
"""