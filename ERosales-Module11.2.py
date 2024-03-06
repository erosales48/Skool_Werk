# Edgar Rosales
# 06MAR2024
# Module 11.2

# Create a program with a recursive function that accepts an integer argument, n,
# and prints the number of 1 up to and including n.
# Then, write a non-recursive method that takes an integer argument, n,
# and prints the number of 1 up to and including n.
# 1. In your code documentation include an explanation of each functions approach to solving the problem.
# 2. Include test code that will not allow a negative or 0 value.
# 3. In your display, include which function is being invoked at both the start and end of the output.


# Recurring function uses the stack as solution for counting up to a top value entered by user.
# the loop goes negative from the value given, then as the stacks resolve at the end it will print
# the values in reverse using first in last out order.
def recurring_print(n):
    if n > 1:
        recurring_print(n - 1)
    print(n)


# Non-recursive function, just uses for range commands
def count_up(n):
    for x in range(n):
        print(x + 1)


# Function to get input from user, and validate it's a positive integer, returns the value once validated.
def get_input():
    verify = False
    while verify is False:
        try:
            number = 0
            while number == 0:
                number = int(input("Enter last number to count to:  "))
                if number <= 0:
                    print("Invalid input! number must be a positive value")
                    number = 0
                else:
                    verify = True
                    return number
        except Exception as err:
            print(err, 'error')


# Main function
def main():
    print('Welcome to count UP!')
    print('This program will count up to input with 2 methods')
    top = get_input()
    print('this iteration is done recursively through recurringPrint function')
    recurring_print(top)
    print('That was recursive recurringPrint function')
    print('This will be non-recursive function count_up')
    count_up(top)
    print('That was the non-recursive function count_up')


if __name__ == '__main__':
    main()
