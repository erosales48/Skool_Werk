# Edgar Rosales
# 09Feb2024
# Module 5.2 assignment:
# Prompt user for filename
# Prompt user for their name
# Prompt user for their street address
# Prompt user for their phone number
# Write username, street address, and phone number to a comma-separated line that user
# typed in step 1, Once the data has been written to the file your program should read
# the file and display the contents
# save the data as Edgar_data.txt

# This program will get input from user and write it to a file as a record.

# Function for getting file to write data to
def get_filename_for_write():
    try:
        filename = input('Please name file to create: ')

        # Make sure to add extension if user did not
        if (filename[-3] + filename[-2] + filename[-1]) != 'txt':
            filename = filename + '.txt'

        return filename

    except Exception as err:
        print(err, ' error')


# Function to get file for reading from
def get_filename_to_read():
    filename = ''
    while filename == '':
        try:
            filename = input('Please enter file to retrieve: ')

            # if used did not add extension add it
            if (filename[-3] + filename[-2] + filename[-1]) != 'txt':
                filename = filename + '.txt'

            # Check to see if file exists
            testfile = open(filename, 'r')
            testfile.close()

            # If files is found return filename to call
            return filename

        except FileNotFoundError:
            # exception results
            print('File not found')

            # initiate again
            again = ''

            # start response loop, until again is not null
            while again == '':
                again = input('Try again Y/N? ')
                again = again.lower()

                # ends loop setting filename to null causing function to repeat
                if again == 'y':
                    filename = ''

                # ends loop with special name of file, and returns it to function call
                elif again == 'n':
                    filename = 'BRK'
                    return filename

                # validate user input, make user re-enter response on fail
                elif again != 'y' or again != 'n':
                    print('Error not Y or N, please only use Y or N')
                    again = ''


# Function to enter fields into record
def enter_data():
    # Writes the fields to a single line record, comma separated
    # open the file for input
    outfile = open(get_filename_for_write(), 'w')
    # Get record fields from user
    user_name = input('Enter your name: ')
    user_address = input('Enter your address: ')
    user_phone = input('Enter phone number: ')
    # add fields to the record as one line, comma separated
    outfile.write(user_name + ',')
    outfile.write(user_address + ',')
    outfile.write(user_phone)
    # Close the file
    outfile.close()


# Function to get records
def read_data():
    # open the fie
    filename = get_filename_to_read()

    if filename == 'BRK':
        print('Return to main menu')

    else:
        infile = open(filename, 'r')

        # Get first Record
        record = infile.readline()

        # Loop for each record
        while record != '':
            # set variables
            index = 0
            break1 = 0
            break2 = 0
            # grab one character from the line, one at a time. looking for the delimiter
            for ch in record:
                if ch == ',':
                    # if this is the first delimiter found assign the index value to it
                    if break1 == 0:
                        break1 = index
                    # second delimiter if first has been used
                    elif break2 == 0:
                        break2 = index
                # iteration
                index += 1

            # Print the separated fields, had to read ahead to find this.
            user_name = record[0:break1]
            user_address = record[(break1 + 1):break2]
            user_phone = record[(break2 + 1):]
            print('name:', user_name + '\n')
            print('address: ', user_address + '\n')
            print('phone number:', user_phone + '\n')

            # get next record
            record = infile.readline()
        # close the file
        infile.close()
        copyfile(filename)


# Function to copy final file to Edgar_data.txt
def copyfile(file):

    # open original file for reading, open new file to write copy to
    with open(file, 'r') as cfile, open('Edgar_data.txt', 'w') as Edata:

        # Get first record
        record = cfile.readline()

        # Loop to copy each record in the file, breaking when null is found
        while record != '':
            # Copy the record
            Edata.write(record)
            # Go to next line
            record = cfile.readline()

    print('data copied')


# Main program, calls the functions to add file read file and quit
def main():
    print('Welcome to datastore\n\n')
    response = ''

    # Main loop for program
    while response == '':
        response = int(input('Please enter 1 to add file, 2 to read file, 3 to quit: '))
        if response == 1:
            enter_data()
            # reset response to repeat loop
            response = ''

        elif response == 2:
            read_data()
            # reset response to repeat loop
            response = ''

        elif response == 3:
            # this ends the loop
            print('Goodbye')

        else:
            # print message to user for Validation for instructions
            print('Please enter number 1, 2 or 3 only')
            # reset response to repeat loop
            response = ''


main()
