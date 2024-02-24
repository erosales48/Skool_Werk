# Edgar Rosales
# 24Feb2024
# Module 8.2 assignment: Stocks

# Create a program that includes a dictionary of stocks.
# Your dictionary should include at least 10 ticker symbols.
# The key should be the stock ticker symbol and the value should be the current price of the stock
# (the values can be fictional).
# Ask the user to enter a ticker symbol.
# Your program will search the dictionary for the ticker symbol and then print the ticker symbol and the stock price.
# If the ticker symbol is not located, print a message indicating that the ticker symbol was not found.

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


# Define dictionary
stocks = dict(HAL=35.21, VOO=466.78, PANW=282.09, SCHD=77.89, ABBV=178.09, LLY=769.54, TSLA=191.67, AVGO=1296.37,
              JEPI=56.88, O=52.91, F=12.14, QQQM=179.81)


# Function to get stock price from dictionary
def fetch_stock(symbol):
    stock = stocks.get(symbol, 'Security not found')
    return stock


# Function to request user input for ticket symbol
def get_symbol():
    symbol = input('Please enter ticker symbol:  ')
    print()
    symbol = symbol.upper()
    return symbol


# Main program
def main():
    # Welcome message
    print('Welcome to stock quoter\n')
    # Warning not to use this in real world
    print(f'{Color.YELLOW} All prices not up to date do not use as investment information!{Color.RESET}')
    # initialize loop variable
    again = 'y'
    # start of main loop
    while again == 'y':
        # function calls to get user input and price from dictionary
        symbol = get_symbol()
        stock = fetch_stock(symbol)
        if stock == 'Security not found':
            print(f'{Color.RED}{stock}{Color.RESET}')
        else:
            print(f'{symbol} = {Color.GREEN}${stock:,.2f}{Color.RESET}')
        # Secondary loop to validate user response to continue
        validate = False
        while validate is False:
            again = input('Another symbol (Y/N)? ')
            again = again.lower()
            if again != 'y' and again != 'n':
                print('Please answer only Y or N\n')
            else:
                validate = True
    print('Have a nice day')


# standard main call
if __name__ == "__main__":
    main()
