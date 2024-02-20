# Edgar Rosales
# 16Feb2024
# Module 6.2 assignment:

# Write a program that acquires a String containing a person’s first, middle, and last names,
# and then display their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.

# Function to get full name
def getname():
    # Initialize variable
    validation = False
    # Loop will request name until name passes validation
    while validation is False:
        fullname = input('\nPlease enter your full name:  ')
        # Calls validation function to make sure no digits are used
        if validate_no_digits(fullname):
            # If no digits are found it returns the name
            return fullname
        else:
            print('\nDo not use numbers in name')


# Function to validate no digits in string
def validate_no_digits(test_string):
    # For loop checks each character in the string for a digit, returns false if found
    for char in test_string:
        if char.isdigit():
            return False
    return True


# Function takes name string and slices it to initials
def make_initials(name):
    # Initialize variables
    index = 0
    index_list = []
    # slice string to find blank spaces
    for char in name:
        index += 1
        if char == ' ':
            # If space is found, add index to list, nuber is already one higher to point at character after space
            index_list.append(index)
    # Start initials string with the first character
    initials = name[0] + '.'
    # For Loop adds the sliced initials from the list
    for initial in index_list:
        initials = initials + ' ' + name[initial] + '.'
    # after initials string is complete, ensure its capitalized.
    initials = initials.upper()
    # return the completed initials string
    return initials


# Main Function, that's all
def main():
    # Welcome message
    print('\nWelcome to the initializer2000')
    # Initialize variable.
    repeat = 'Y'
    # Main loop for program, to decide when to terminate program
    while repeat != 'N':
        # call function to request name from user
        name = getname()
        # calls function to create the initials and prints them
        print(make_initials(name))
        # Repeat Loop, ends program if any key the y is entered
        repeat = (input('Another (Y/N):  ')).upper()
        # only use the first character in case they type Yes
        if repeat[0] != 'Y':
            repeat = 'N'
            print('\nHave a nice day!')

# standard main call
if __name__ == "__main__":
    main()
