## Programming Project 10
## Files (Input/Output and Looping to process files)

import os 

def main():
    ## Calling all functions
    readFile()
    printFile()
    deleteFile()
      
## Function to create and Write to the File
def writeFile():
    # Declaring global variable
    global names
    # Open a file 
    names = open('names.txt', 'w')
    # Storing the list of names in a 2D Array
    listOfNames = [["Ambrosa", "Briona", "Chloe", "Donte", "Elijah"],
                    ["Kensworth", "Lane", "McLamb", "Noggins", "O'Neil"]]
    # Inital index counter variable
    index = 0
    # For Each loop regarding the indexes of listOfNames list
    for index in range(len(listOfNames[0])):
        # Declaring the variables of the indexes
        first = listOfNames[0][index]
        last = listOfNames[1][index]

        # Write the list data to the file.
        names.write(first + " " + last + "\n")
        
    # Close the file.
    names.close()

## Function to Read the file ONLY
def readFile():
    # Calling the write file function to write data to the file
    writeFile()
    # Open the file for Read only
    names = open('names.txt', 'r')
    # Closing the file
    names.close()
    
## Function to Print contents of file and display the total
def printFile():
    # Open the file for Read only
    names = open('names.txt', 'r')
    # Initial counter variable
    total = 0

    # For Each loop regarding the Lines of each name in the file
    for line in names:
        # Separating the Lines
        line = line.strip()
        # Print the results of the line
        print(line)
        # Increase total counter
        total += 1

    # Print total amount of lines included in the file
    print("Total names:", total)
    # Closing the file
    names.close()

## Function to delete the file
def deleteFile():
    # If/Else statement to check if the file exist
    if os.path.exists('names.txt'):
        # Removes the necessary file
        os.remove('names.txt')
        # Displays successful deletion message
        print("The name file has been deleted successfully")
    else: 
        # Displays the failure message
        print("The name file has NOT been deleted, lets try again!")
    ## End If

# Call the main function.
main()

## Final Reflection :'(
"""
Good lord professor, this project def gave me a run for my money, but 
I was able to finally understand it properly to know what to write and
how it worked.
"""