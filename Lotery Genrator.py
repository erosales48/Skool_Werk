# the lottery generator from the textbook

import random

MAX_DIGITS = 5
START = 1
END = 70
MEGA = 25


class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


def white_ball():
    numbers = [0] * MAX_DIGITS
    for index in range(MAX_DIGITS):
        accept = False
        while accept is False:
            ball = random.randint(START, END)
            if ball not in numbers:
                numbers[index] = ball
                accept = True

    return numbers


def megaball():
    number = random.randint(START, MEGA)
    return number


def main():
    response = 'y'
    while response == 'y':
        numbers = white_ball()
        mega = megaball()
        numbers.sort()
        print('Here are your Lottery numbers:')
        for index in range(MAX_DIGITS):
            print(f'{Color.WHITE}{numbers[index]}{Color.RESET}', end=' ')

        print(f'{Color.YELLOW} {mega}{Color.RESET}')
        response = input('Would you like another? ')
        response.lower()


# standard main call
if __name__ == "__main__":
    main()
