# Edgar Rosales
# 16Feb2024
# Module 6.2 assignment:

# Create a Tuple initialized with 15 to 25 related values such as automobile types, states, names, etc.
# Complete the following steps using the Tuple you have just created.
# Initialize with values.
# Display the contents in a single statement.
# Iterate through the collection displaying the output as a complete sentence using each value.
# Use the f-string format to control the output.
# Repeat the output in reverse order using a different context string.
# Test your program until it works, and the output looks readable and understandable.


# Function defining tuple
def get_lance():
    LANCE = (('AS7-A', 'Atlas', 'Assault', 100, 10702000.0),
             ('BLR-3M', 'Battlemaster', 'Assault', 85, 8967905.0),
             ('CPLT-C4', 'Catapult', 'Heavy', 65, 5830963.0),
             ('TDR-5S', 'Thunderbolt', 'Heavy', 65, 5396023.0),
             ('WHM-7M', 'Warhammer', 'Heavy', 70, 6771384.0))
    return LANCE


# Function to print tuple backwards
def print_lance():
    # initialize variables
    count = 0

    # Get record of 2 dimensional tuple
    for mech in get_lance():

        # Initialize in loop variables
        count += 1
        index = 0

        # print line number
        print(f'Mech {count}. ', end = ' ')

        # Get fields from record in order and label each, contingent on index number
        for element in mech:
            index += 1
            if index == 1:
                print(f'Model: {element}', end = ' ')
            elif index == 2:
                print(f'Name: {element}', end = ' ')
            elif index == 3:
                print(f'Class: {element}', end = ' ')
            elif index == 4:
                print(f'Weight: {element} Tons', end = ' ')
            elif index == 5:
                print(f'Cost: {element:,.2f} C-Bills')

    # Call function to get total cost from all records then print it
    print(f'Total cost of lance {lance_cost(get_lance()):,.2f} C-Bills')


def print_lance_reverse():
    # initialize variables
    count = 0

    # Get record of 2 dimensional tuple in reverse order
    for mech in get_lance()[::-1]:

        # Initialize in loop variables
        count += 1
        index = 0

        # print line number
        print(f'Mech {count}. ', end=' ')

        # Get fields from record in order and label each, contingent on index number
        for element in mech:
            index += 1
            if index == 1:
                print(f'Model: {element}', end=' ')
            elif index == 2:
                print(f'Name: {element}', end=' ')
            elif index == 3:
                print(f'Class: {element}', end=' ')
            elif index == 4:
                print(f'Weight: {element} Tons', end=' ')
            elif index == 5:
                print(f'Cost: {element:,.2f} C-Bills')

    # Call function to get total cost from all records then print it
    print(f'Total cost of lance {lance_cost(get_lance()):,.2f} C-Bills')


# Function to display only heavy mechs and thir associated total cost
def print_heavy_lance():

    # initialize variables
    count = 0
    mech_list = []

    # begin loop for records calling function defining tuples
    for mech in get_lance():

        # select only records matching the Heavy label
        if mech[2] == 'Heavy':

            # Initialize loop variables and make copy or record into list to pass to cost function
            mech_list.append(mech)
            count += 1
            index = 0

            # print line number
            print(f'{count}.', end = ' ')

            # Get fields from record in order and label each, contingent on index number
            for element in mech:
                index += 1
                if index == 1:
                    print(f'Model: {element}', end = ' ')
                elif index == 2:
                    print(f'Name: {element}', end = ' ')
                elif index == 3:
                    print(f'Class: {element}', end = ' ')
                elif index == 4:
                    print(f'Weight: {element} Tons', end = ' ')
                elif index == 5:
                    print(f'Cost: {element:,.2f} C-Bills')

    # Call function sending list and getting total cost return,then print it
    print(f'Total cost of lance {lance_cost(mech_list):,.2f} C-Bills')


# Function to display only Assault mechs and thir associated total cost
def print_assault_lance():

    # Initialize variables
    count = 0
    mech_list = []

    # begin loop for records calling function defining tuples
    for mech in get_lance():

        # select only records matching the Assault label
        if mech[2] == 'Assault':

            # Initialize loop variables and make copy or record into list to pass to cost function
            mech_list.append(mech)
            count += 1
            index = 0

            # print line number
            print(f'{count}.', end=' ')

            # Get fields from record in order and label each, contingent on index number
            for element in mech:
                index += 1
                if index == 1:
                    print(f'Model: {element}', end = ' ')
                elif index == 2:
                    print(f'Name: {element}', end = ' ')
                elif index == 3:
                    print(f'Class: {element}', end = ' ')
                elif index == 4:
                    print(f'Weight: {element} Tons', end = ' ')
                elif index == 5:
                    print(f'Cost: {element:,.2f} C-Bills')

    # Call function sending list and getting total cost return,then print it
    print(f'Total cost of lance {lance_cost(mech_list):,.2f} C-Bills')


# Function to add total cost of records received
def lance_cost(lance):

    # Initialize variable
    total = 0

    # For loop to sum up cost
    for cost in lance:
        total += cost[4]

    # return total cost
    return total


# Function to display menu, get user input and retun it
def menu_call():
    print('          MENU')
    print(' (1) Show all Mechs')
    print(' (2) Show all Mechs in reverse oder')
    print(' (3) Show Heavy Mechs')
    print(' (4) Show Assault Mechs')
    user_input = input('Please enter choice "x" to exit: ')

    return user_input

# Main function
def main():

    # Welcome message
    print('Welcome to Mechlab'+'\n\n')

    # Initialize variable
    user_input = ''

    # Loop continues until exit character is selected
    while user_input != 'x' or user_input != 'X':
        user_input = menu_call()
        if user_input == 'x' or user_input == 'X':
            print('Thanks for visiting have a nice day')
            break
        elif user_input == '1':
            print('\n\n')
            print_lance()
            print()
        elif user_input == '2':
            print('\n\n')
            print_lance_reverse()
            print()
        elif user_input == '3':
            print('\n\n')
            print_heavy_lance()
            print()
        elif user_input == '4':
            print('\n\n')
            print_assault_lance()
            print()
        else:
            print('Please use ony menu choices in menu')

main()
