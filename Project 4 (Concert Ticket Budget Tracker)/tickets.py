## Programming Project 4
## Concert Ticket Budget Tracker (Repetition Structures)

"""
This budget tracker/calculator will display a series of question regarding the users
total budget for the tickets, the kind of tickets, and the amount of tickets they'd
like to get. It will display their total amount left and the amount of the specific
tickets purchased if provided with a budget of over $20
"""


## Storing the necessary variables and constants required to perform the necessary loop
budget:float
restart:str
ticketType:str
amountOfTickets:int
costTotal:float
response:str
remainder:float

## Storing the constant prices for the different tickets
VIPTICKET = int(50)
STANDARDTICKET = int(30)
BUDGETTICKET = int(20)

## Asking for the users budget
budget = float(input("Welcome to the Concert Budget Tracker! Before we get started, What's your budget looking like? (How much munyun you got?!): $"))

## While the user still has money left over, or until they say no, continue to ask about ticket sales
while budget >= 20: 

    ## Asking the initial purchase tickets question to loop a response for users to exit or continue
    restart = str(input("Would you like to purchase tickets? "))

    if restart == "yes" or restart == "yes":
        ## Asking what type of ticket they want (VIP, Standard, Budget)
        ticketType = str(input("Alrighty! What kind of tickets would you like to purchase? You can choose from our options: VIP, Standard, or Budget (Only allowed to choose one type at a time): "))

        if ticketType == "VIP" or ticketType == "vip":
            ## Asking for the total amount of tickets they need
            amountOfTickets = int(input("And how many tickets would you like to purchase?: "))

            ## Calculating the cost of the VIP tickets with the amount needed in order to create the general total
            costTotal = amountOfTickets * VIPTICKET

            ## Asking user for confirmation and displaying their total amount
            print(f"Are you really trying to purchase ${costTotal} worth of tickets?!")
            response = str(input("Please Enter Yes or No: "))

            ## Comparing the user's acceptance and their cost total with their starting budget
            if (response == "yes" or response == "Yes") and (budget >= costTotal):

                ## Calculating the remaining dollars left
                remainder = budget - costTotal

                ## Displaying their total cost, their tickets, and their remaining budget.
                print(f"...okay Big Money! We BALL! Enjoy the special Big Pimpin' Tickets! Cue the Bottle girls! Here's what you have left playa: ${remainder} and {amountOfTickets} tickets!")

                # Reinstating the budget with the remainder of what they bought
                budget = remainder

            else:
                print(f"I'm sorry, Lets start over!")

            ## EndIf
            
        elif ticketType == "Standard" or ticketType == "standard":

            ## Asking for the total amount of tickets they need
            amountOfTickets = int(input("And how many tickets would you like to purchase?: "))

            ## Calculating the cost of the Standard tickets with the amount needed in order to create the general total
            costTotal = amountOfTickets * STANDARDTICKET

            ##Asking user for confirmation and displaying their total amount
            print(f"Are you trying to purchase ${costTotal} worth of tickets?! ")
            response = str(input("Please Enter Yes or No: "))

            if (response == "yes" or response == "Yes") and (budget >= costTotal):
                remainder = budget - costTotal

                ## Displaying their total cost, their tickets, and their remaining budget.
                print(f"Okay! Here's what you have left: ${remainder} and {amountOfTickets} tickets")

                # Reinstating the budget with the remainder of what they bought
                budget = remainder

            else:
                print(f"I'm sorry, Lets start over!")

            ## EndIf

        elif ticketType == "Budget" or ticketType == "budget":

            ## Asking for the total amount of tickets they need
            amountOfTickets = int(input("And how many tickets would you like to purchase?: "))

            ## Calculating the cost of the Budget tickets with the amount needed in order to create the general total
            costTotal = amountOfTickets * BUDGETTICKET

            ##Asking user for confirmation and displaying their total amount
            print(f"Are you trying to purchase ${costTotal} worth of tickets?! ")
            response = str(input("Please Enter Yes or No: "))

            if (response == "yes" or response == "Yes") and (budget >= costTotal):
                remainder = budget - costTotal

                ## Displaying their total cost, their tickets, and their remaining budget.
                print(f"Okay! Here's what you have left: ${remainder} and {amountOfTickets} tickets")

                # Reinstating the budget with the remainder of what they bought
                budget = remainder

            else:
                print(f"I'm sorry, Lets start over!")

            ## EndIf

        ## If the user doesn't enter an acceptable ticket type        
        else:
            print("HUH? What ticket is that? I'm a bit confused, We may have to run that again sweetheart.")
        
        ## EndIf

    ## If user says No or give invalid response        
    else:
        print("Oops, my bad! I'll see myself out of your pockets now! Goodbye!")

    ## EndIf

## If budget is zero, prevent the ticket sales 
else:
    print("Sorry hun, it seems to appear that you're all out of money. (HIDE THE MONEY Y'ALL ITS BROKE PEOPLE AROUND!)")
    print("Oops, my bad! I'll see myself out of your pockets now! Goodbye!")

## EndIf

## Reflection Time!

"""
While creating this program, I shortly began to struggle with the variables
and the loops and conditions to implement the necessary restrictions. Quickly 
came to the realization that I should have created a flowchart, because this 
started to get messy really quickly. I started by declaring the necessary 
variables and constants like the cost of each of the tickets and the variables 
for saving the users inputs, however when I began to work on creating the 
WHILE-loop, I've had to repeatedly go back and add in the declaration of the 
new variables. I've also began by asking a series of questions to the user, 
then saving their inputs as variables to use in the WHILE-loop, but as I've 
tested the program, I've noticed a few of the restrictions applying outside of 
the desired results, and certain responses wouldn't loop again. After some 
review of the Python provided class textbook, attending Prof.Pigatt's class, 
and reading the Chapter 4 companion text, I went back and rearranged the 
structure of my WHILE-loop, placed the input questions inside the WHILE-loop, 
added new restrictions (in case user uses lowercase, and/or budget is enough to 
purchase the requested tickets), added an exit strategy for certain responses 
(in case user no longer wants to purchase or doesn't have the funds to), and 
created new variables out of repeated calculations I was performing within 
the IF/ELSE statements (the costTotal and remainder variable). After retesting, 
I felt more confident in the program running correctly, there's still minor issues 
I'd like to fix (I figured I need to implement FOR-loops, arrays, and other 
conditions that we will probably get to in the future to simplify some of the 
repeated code, and to help clean up the loop).
"""
