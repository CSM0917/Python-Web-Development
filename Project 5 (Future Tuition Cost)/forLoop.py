## Programming Project 5
## Tuition Projection (For Loops)

## Declaring the variable type
someUniversity:float
## Storing the increase percentage in decimal form as a variable
INCREASE = float(0.03)
## Storing the cost of tuition as a float variable
someUniversity = float(27000)

## For Each Year (1-5), Add the tuition cost to the increase amount
for year in range (1,6):
    ## Display Year and Tuition
    print(f"Year: {year}, Tuition: ${someUniversity}")
    ## Appyling the interest cost towards the tuition cost
    newTuition = round(someUniversity + (someUniversity * INCREASE), 2)
    ## Storing the university tuition cost with the new tuition cost after calculations
    someUniversity = newTuition