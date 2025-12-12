## Programming Project 5
## Tuition Projection (While Loops)

## Declaring the variable types
someUniversity:float
year:int
## Storing the increase percentage in decimal form as a variable
INCREASE = float(0.03)
## Storing the cost of tuition as a float variable and the initial year
someUniversity = float(27000)
year = 1

## While Each Year is Less than or Equal to 5, Add the tuition cost to the increase amount
while year <= 5:
    ## Display Year and Tuition
    print(f"Year: {year}, Tuition: ${someUniversity}")
    ## Appyling the interest cost towards the tuition cost
    newTuition = round(someUniversity + (someUniversity * INCREASE), 2)
    ## Storing the university tuition cost with the new tuition cost after calculations
    someUniversity = newTuition
    ## Increase the year count by 1 each time the loop iterates
    year = year + 1