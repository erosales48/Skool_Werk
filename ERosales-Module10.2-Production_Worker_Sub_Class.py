# Edgar Rosales
# 03Mar2024
# Module 10.2 assignment: Production worker subclass

# Create two classes, the Employee class and the ProductionWorker class that inherits from the Employee class.
# The Employee class will have four fields: the employee name, employee gender, employee hourly pay rate,
# and the employee number. The ProductionWorker class will extend the Employee class
# and have one additional field: the shift number, such as day shift (1), swing shift (2), and graveyard (3).
# Write setters and getters (attribute managers) for all fields in both classes.

# 1. Write a Main class that uses these classes.
# 2. In the Main class, create two instances of each class. Set all field values using setters and getters.
# 3. Set the values in the code requiring no user input.
# 4. Using these four class instances, displaying the information to the user of the application, making the
#    output very readable and understanding.

# Class for Employee
class Employee:
    def __init__(self, name, gender, hourly_pay_rate, employee_id):
        self._name = name
        self._gender = gender
        self._hourly_pay_rate = hourly_pay_rate
        self._emp_number = employee_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_hourly_pay_rate(self):
        return self._hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self._hourly_pay_rate = hourly_pay_rate

    def get_emp_number(self):
        return self._emp_number

    def set_emp_number(self, emp_number):
        self._emp_number = emp_number


# ProductionWorker is a subclass of Employee
class ProductionWorker(Employee):
    def __init__(self, name, gender, hourly_pay_rate, employee_id, shift_number):
        super().__init__(name, gender, hourly_pay_rate, employee_id)
        self._shift_number = shift_number

    def get_shift_number(self):
        return self._shift_number

    def set_shift_number(self, shift_number):
        self._shift_number = shift_number


# Function to fetch data from file
def load_employee_data():
    # Assuming data is stored in a file named 'employee_data.txt'
    # with format: emp_number,name,gender,hourly_pay_rate,shift_number
    employee_data = {}
    with open('employee_data.txt', 'r') as file:
        for line in file:
            emp_number, name, gender, hourly_pay_rate, shift_number = line.strip().split(',')
            if shift_number.isdigit():
                employee_data[emp_number] = {
                    'name': name,
                    'gender': gender,
                    'hourly_pay_rate': float(hourly_pay_rate),
                    'shift_number': int(shift_number)
                }
            else:
                employee_data[emp_number] = {
                    'name': name,
                    'gender': gender,
                    'hourly_pay_rate': float(hourly_pay_rate)
                }
    return employee_data


# Main class will load the employee data from a file and display it for the user
class Main:
    def __init__(self):
        # Load employee data from file
        self.employee_data = load_employee_data()

        # Display employee info
        self.display_employee_info()

    # Method to display the data
    def display_employee_info(self):
        print("    EID\t\t Name\t\t\tGender\tPay/Hour\t Shift")
        print("-----------------------------------------------------------")
        for emp_number, emp_info in self.employee_data.items():
            info_str = (f"{emp_number:>8}:\t{emp_info['name']:14}\t"
                        f"{emp_info['gender']:7}\t${emp_info['hourly_pay_rate']:<10,.2f}\t")
            if 'shift_number' in emp_info:
                info_str += f" Shift {emp_info['shift_number']}"
            else:
                info_str += f" Exempt"
            print(info_str)


# Creating an instance of the Main class to run the program
main = Main()
