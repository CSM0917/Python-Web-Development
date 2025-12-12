## Programming Project 1
## Weekly Fitness Tracker (Input-Processing-Output)

## Declaring variables for storing the users input and their steps
userName:str
stepsGoal: int
stepsTaken:int
stepsNeeded:int


## Welcoming user and Getting the users name
print("Welcome to Weekly Fitness Tracking!")
print("Enter your preferred name: ")
userName = str(input())

## Getting amount of steps user would like to take (goal)
print("Hey", userName, ", What is your step goal number this week?")
stepsGoal = int(input())

## Getting amount of steps taken by user
print("Hey", userName, ", How many steps did you take this week?")
stepsTaken = int(input())

## Calculating the steps they have left in their goal
stepsNeeded = stepsGoal - stepsTaken

## Telling the user how many steps they have left
print("Great job", userName, "! You just have", stepsNeeded, "steps left to go!")


## Reflection Time!
"""
To create this tracker I've started with considering ways 
to make sure the user does whats intended. Using my
previous knowledge of C# and Javascript, I'm familiar
with declaring variables and constants. While using
my flowchart as reference, I've began by declaring my
necessary variables that I'll be storing. While writing,
I did not want to store the users name and not use it,
so I've included that variable throughout the rest of the
process. Upon completion, I began to think of ways of 
informing the user when the calculations has ended, asking
the user if they'd like to re-enter another entry, or if 
they'd like to continue to update their tracker.
"""