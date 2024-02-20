# Edgar Rosales
# 16Feb2024
# Module 6.2 assignment:

# Write a program that acquires a String containing a person’s first, middle, and last names,
# and then display their first, middle, and last initials.
# For example, if the user enters John William Smith, the program should display J. W. S.

def getname():
    validation = False
    while validation is False:
        fullname = input('\nPlease enter your full name:  ')
        if validate_no_digits(fullname):
            return fullname
        else:
            print('\nDo not use numbers in name')


def validate_no_digits(test_string):
    for char in test_string:
        if char.isdigit():
            return False
    return True


def make_initials(name):
    index = 0
    index_list = []
    for char in name:
        index += 1
        if char == ' ':
            index_list.append(index)
    initials = name[0] + '.'
    for initial in index_list:
        initials = initials + ' ' + name[initial] + '.'
    initials = initials.upper()
    return initials


def main():
    print('\nWelcome to the initializer2000')
    repeat = 'Y'
    while repeat != 'N':
        name = getname()
        print(make_initials(name))
        repeat = (input('Another (Y/N):  ')).upper()
        if repeat != 'Y':
            repeat = 'N'
            print('\nHave a nice day!')


if __name__ == "__main()__":
    main()
