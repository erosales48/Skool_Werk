# Edgar Rosales
# 29Feb2024
# Module 9.2 assignment: Student class

# Create a student class that implements the following class diagram, that will calculate
# and display student cumulative GPA. Your program will then use the methods of the student
# class to accomplish the following:
# 1. Prompt the user for the first and last name of teh student
# 2. Create a student object by passing the first and last name to the __init__ method.
# 3. Create a loop that prompts the user for the following: the credits and grade for each
#    course the student has taken.
# 4. Once the user ends the loop, display student's cumulative GPA.

# Constants
A_GRADE = 4.0
B_PLUS_GRADE = 3.5
B_GRADE = 3.0
C_PLUS_GRADE = 2.5
C_GRADE = 2.0
D_GRADE = 1.0
F_GRADE = 0.0


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []

    def add_course(self, course_name, credits, grade):
        self.courses.append({"course_name": course_name, "credits": credits, "grade": grade})


# Function to validate no digits in string
def validate_no_digits(test_string):
    # For loop checks each character in the string for a digit, returns false if found
    valid = False
    while valid is False:
        for char in test_string:
            if char.isdigit():
                return False
            else:
                valid = True
    return True


# Function to get user input for student name
def get_first_name():
    # Initialize variable
    validation = False
    # Loop will request name until name passes validation
    while validation is False:
        name = input("\nPlease enter student's first name:  ")
        # Calls validation function to make sure no digits are used
        if validate_no_digits(name):
            # If no digits are found it returns the name
            return name
        else:
            print('\nDo not use numbers in name')


# Function to get user input for student name
def get_last_name():
    # Initialize variable
    validation = False
    # Loop will request name until name passes validation
    while validation is False:
        name = input("\nPlease enter student's last  name:  ")
        # Calls validation function to make sure no digits are used
        if validate_no_digits(name):
            # If no digits are found it returns the name
            return name
        else:
            print('\nDo not use numbers in name')


def get_student_courses(student1):
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course_name = input("Enter the name of course {}: ".format(i+1))
        credits = float(input("Enter the credits for course {}: ".format(i+1)))
        grade = input("Enter the grade for the course {}: ".format(i+1))
        student1.add_course(course_name, credits, grade)
    print("Courses taken by", student1.first_name, student1.last_name)
    for course in student1.courses:
        print("Course:  {}, Credits: {}, Grade: {}".format(
            course["course_name"], course["credits"], course["grade"]))


def main():
    student1 = Student(get_first_name(), get_last_name())
    print("First name: ", student1.first_name)
    print("Last name: ", student1.last_name)
    get_student_courses(student1)


# standard main call
if __name__ == "__main__":
    main()
