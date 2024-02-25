# ERosales-Mod4.2-Miles2Kilometers.py
# Edgar Rosales
# 26January2024
# Module 4.2 assignment - create a function that converts Miles to Kilometers

# This Program will enter a loop to call a function, which will ask user for Miles
#  it will then call another function to convert Miles to Kilometers, then give the
# result to the user, it will then return to main and main will ask for repeat.


# Constants
M2KCONSTANT = 1.60934


# Function to convert Miles to Kilometers
def miles2kilometers(miles):
    kilometers = miles * M2KCONSTANT
    return kilometers


# Function to ask user for Miles
def askformiles():
    mile = float(input('Please enter miles: '))
    kilometer = miles2kilometers(mile)
    print(f' {mile}Miles = {kilometer:.2f}Kilometers')


# Main, Intro and loop for repeat function call
def main():
    again = 'y'
    print('Welcome to Miles to Kilometers conversion' + '\n' + '\n')
    while again == 'y':
        askformiles()
        again = input('\n' + '\n' + 'Would you like to do another conversion? y/n ')
        again = again.lower()


main()
