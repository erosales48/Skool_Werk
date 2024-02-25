
def write_data():
    # Open a file named philosophers.txt
    # Open a file to write not to append
    outfile = open('philosophers.txt', 'w')

    # Write the names of the three philosophers
    # to the file
    # \n is the newline character
    outfile.write('John Cena\n')
    outfile.write('Hulk Hogan\n')
    outfile.write("""Randy "Macho-Man" Savage\n""")

    # Close the file
    outfile.close()


def read_data():
    # Open the file philosophers.txt
    # Read File
    infile = open('philosophers.txt', 'r')

    # Read the file contents
    # Assign contents to variable
    file_contents = infile.read()

    # close the file
    infile.close()

    # Print the data that was read into memory
    print(file_contents)


def put_sales():
    # Get the number of days.
    num_days = int(input('For how many days do you have sales? '))

    # Open a new file named sales.txt
    sales_file = open('sales.txt', 'w')

    # Get amount of sales for each day and add it to the file
    for count in range(1, num_days + 1):
        # Get the sales for a day
        sales_day = float(input(f'Enter the sales for day #{count}: '))

        # Write the sales amount to the file.
        sales_file.write(f'{sales_day}\n')

    # Close the file
    sales_file.close()
    print('Data written to sales.txt')


def get_sales():
    sales_file = open('sales.txt', 'r')
    line = sales_file.readline()
    total = 0.0
    count = 1
    while line != '':
        amount = float(line)
        print(f'{count}. ${amount:.2f}')
        count += 1
        total = total + amount
        line = sales_file.readline()

    sales_file.close()
    print(f'Total Sales = ${total:.2f}')
    average = total / (count - 1)
    print(f'Average daily sales ${average:.2f}')


def ask_request():
    print('Welcome\n\nPlease chose\n E to reset\n P to print')
    print(' A to add numbers to the file\n C to add them together')
    print(' S for Enter Sales\n K for Read Sales')
    response = input('enter: ')
    response = response.lower()
    if response == 'e':
        write_data()
    elif response == 'p':
        read_data()
    elif response == 'a':
        print('\n\n')
        add_numbers()
    elif response == 'c':
        calculate()
    elif response == 's':
        put_sales()
    elif response == 'k':
        get_sales()
    else:
        print('Input Error')


def add_numbers():
    outfile = open('numbers.txt', 'w')

    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Close the file
    outfile.close()


def calculate():
    # Open file for reading
    infile = open('numbers.txt', 'r')

    # Read three numbers from the file, converting them to integers
    num1 = int(infile.readline())
    num2 = int(infile.readline())
    num3 = int(infile.readline())

    # Close the file
    infile.close()

    # add it all
    total = num1 + num2 + num3

    # Display result
    print(f'The numbers are: {num1}, {num2}, {num3}')
    print(f'Their total is: {total}')


def main():
    print('\n\n START')
    answer = 'y'
    while answer == 'y':
        ask_request()
        answer = input('again Y/N? ')
        answer = answer.lower()


# Call the main function
main()
