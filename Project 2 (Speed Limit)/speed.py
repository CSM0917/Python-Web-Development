## Programming Project 2
## Speed Limit (Decisions and Boolean Logic)

## Declaring variables for storing the users inputs and their results
userName:str
speedLimit:int
userSpeed:int
results:float

## Constant for storing the fines
FIRSTFINE= str("$50")
SECONDFINE = str("$200")

## Welcoming user and Getting the users name
print("Welcome to Speed Limit Calculating!")
userName = input("Enter your preferred name: ")

## Getting speed limit and current speed by user
print("Hey", userName, ", What's the current speed limit in your area?:")
speedLimit = int(input("Miles per hour: "))

print("And what's the current speed of which you're going?")
userSpeed = int(input("Miles per hour: "))

## Calculating the speed limit with the user's current speed to display their results
results = userSpeed - speedLimit

## Using an If/Else statement to display the user's results based off what they've said
if results <= 0:
    print("You are driving within the speed limit. Good job!")
elif results <= 10:
    print(f"You are speeding. Your fine is", FIRSTFINE)
else:
    print(f"You are speeding. Your fine is", SECONDFINE)


## Reflection Time
"""
To create this speed limit calculator, I've started working on 
writing my code prior to my flowchart. That eventually caused 
an issue for me on my "If/Else" statement. First I began 
trying to create the statement based off the "userSpeed -
speedLimit" calculation and quickly came to the realization
that I would not be able to properly print the correct messages
for the proper speed limit results. Then I soon realized I 
can not create the statement with the calculation and the results
without saving the results in some sort of variable. Shortly, 
after reviewing my notes, I came to the realization of saving
the results in a variable, doing the If/Else statement with 
the result variable, and using that variable to compare against 
10 and 0.
"""
