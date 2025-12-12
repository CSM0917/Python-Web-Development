## Programming Project 3
## Movie Rating (Decisions, Boolean Logic, & Repetition Structures)
## Users will enter in their age in order to get back a movie rate suggestion suitable for their age range

## Declaring variable for storing the users age input and the display message
userAge:int

## Storing the Movie Ratings as constants
gRated= str("G: Suitable for all ages.")
pgRated= str("PG: Parental guidance suggested for children under 10")
pgThirteenRated= str("PG-13: Parents strongly cautioned for viewers under 13.")
rRated= str("R: Restricted to viewers aged 17 and above")
ncSeventeenRated= str("NC-17: No one under 17 admitted")

## Asking the user for their age input
print("Welcome to Movie Ratings! Let's find out what kinda movies you're allowed to watch!")
userAge = int(input("Enter your age: "))

## Generic display that wbgins the list of the users movie ratings
print(f"You're in the age range to watch these kind of rated movies: ")

## If/Else statement that compares the age of the user so it can print out the ratings for the movies they can watch.
if userAge <= 9: # Any age less than 9
    print(f"{gRated}") 
elif userAge <= 12: # Any age less than or equal to 12
    print(f"{gRated}")
    print(f"{pgRated}")
elif userAge <= 16: # Any age less than or equal to 16
    print(f"{gRated}")
    print(f"{pgRated}")
    print(f"{pgThirteenRated}")
else: # Any age over or equal to 17
    print(f"{gRated}")
    print(f"{pgRated}")
    print(f"{pgThirteenRated}")
    print(f"{rRated}")
    print(f"{ncSeventeenRated}")

## Reflection Time!
"""
When I originally began creating the program, I kept receiving errors 
indicating that my If/else statement couldn't compare integer with string
despite me declaring the age variable as an integer. I went back and redeclared 
it as an integer again when I prompt the user for age input. Now when beginning 
the If/else statement, it functioned properly with each age range listing each 
suitable movie rating range, however it only showed one response for each age. 
I wanted it to display each movie rating for all ages it suits, eventually 
showing all ratings for anyone inputting an age over 17. 
"""
