## Programming Project 9
## String Arrays (Looping Parallel Arrays)

def main():
    showNames()

## Defining the display name function
def showNames():
    ## Declaring the constant for the list maximum
    ROWS = 5

    ## Declaring the list of people and ages
    people = ["Ambrosa", "Briona", "Chloe", "Donte", "Elijah"]
    age = [25, 26, 35, 43, 58]

    ## Naming the values of the list and declaring them at starting 0
    name = 0
    num = 0

    ## While loop to compare the values of the list variables to the constant
    while name < ROWS and num < ROWS:

        ## Display name and ages
        print(f"Name: {people[name]}, Age:{age[num]}")

        ## Increment the list variables for looping
        name = name + 1
        num = num + 1

## Calling the main function
main()

## Reflection

"""
Originally when I first began this program, I was a bit confused on the
criteria for it, so I wrote with the idea of asking the user to input
names and ages for the list, then display back that entered information.
It worked, I even started working on the defensing for the programming
however, after to speaking with a few classmates, I quickly discovered
that its just inserted names, instead of getting an input from the user.
So I went back, removed alot of code, and reran it to make sure it worked
properly. I'm aware about the For-Loop and using range, but for visual 
and note taking purposes, I used the while loop. I realized, I'm very
quick to rely on a For-Loop so I am challenging myself to work more with 
While-Loops.
"""