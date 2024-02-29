# the lottery generator from the textbook, improved

import random
import tkinter as tk

# Constants
MAX_DIGITS = 5
START = 1
END = 70
MEGA = 25


# Color codes in a class for easy use
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


# Function to generate 5 distinct numbers within the range given
def white_ball():
    numbers = [0] * MAX_DIGITS
    label = ''
    for index in range(MAX_DIGITS):
        accept = False
        while accept is False:
            ball = random.randint(START, END)
            if ball not in numbers:
                numbers[index] = ball
                accept = True
    numbers.sort()
    for index in range(MAX_DIGITS):
        label += str(numbers[index]) + ' '
    return label


# the megaball single random nuber is simple
def megaball():
    number = random.randint(START, MEGA)
    return number


def generate_numbers():
    numbers = white_ball()
    mega = megaball()
    result_label.config(text=f"Lottery numbers: {numbers:^16}  Mega Ball: {mega}  ", fg="blue")


# Main GUI window
root = tk.Tk()
root.title("Lottery Number Generator")

# Button to Generate numbers
generate_button = tk.Button(root, text="Generate Numbers", command=generate_numbers)
generate_button.pack(pady=10)

# Label to display generated numbers
result_label = tk.Label(root, text="", fg="green")
result_label.pack(pady=10)

root.mainloop()

# standard main call
# if __name__ == "__main__":
#     main()
