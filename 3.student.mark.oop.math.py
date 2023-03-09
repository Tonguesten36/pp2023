
# Objectives: 
# • Use math module to round-down student scores to 1-digit decimal upon input, floor() (done)
# • Use numpy module and its array to
#   • Add function to calculate average GPA for a given student (done)
#       • Weighted sum of credits and marks
#   • Sort student list by GPA descending (done)
# • Decorate your UI with curses module (I'll assume that we only need to use curses for output functions,
#       but maybe I'll come back and implement them for input functions as well in the future)
# • Push your work to corresponding forked Github repository

import math
import numpy as np
import curses # Still trying to figuring out how this works

# Data
students_list = []
courses_list = []
marks_list = []

# Objects
class Object:
    def __init__(self, name, id):
        self._name = name
        self._id = id
    
    # Append the object to the list
    def _insert_to_list(self, list):
        list.append(self)
        return list
 
    # Get the name of the obj
    def _get_name(self):
        return self._name
    
    # Get the id of the obj
    def _get_id(self):
        return self._id
    
    # String representation of obj
    def __str__(self):
        return f"Name: {self._name}, ID: {self._id}"

class Student(Object):
    def __init__(self, name, id, dob):
        super().__init__(name, id)
        self.__student_dob = dob

    # Get the d.o.b of the student
    def _get_dob(self):
        return self.__student_dob

    # Compare between two students and return true if specific attributes are identical
    def __lt__(self, other_student):
        return self._id == other_student._id

    # String representation of Student
    def __str__(self):
        return f"Name: {self._name}, ID: {self._id}, D.O.B: {self.__student_dob}"
    
class Course(Object):
    def __init__(self, name, id):
        super().__init__(name, id)
    
    def __str__(self):
        return super().__str__()

    def __lt__(self, other_course):
        return (self._name == other_course._name) or (self._id == other_course._id)

class StudentMark:
    def __init__(self, student_id, course_name, mark):
        self.__student_id = student_id
        self.__course_name = course_name
        self.__student_mark = mark
    
    def _get_course_name(self):
        return self.__course_name 

    def _get_student_id(self):
        return self.__student_id
    
    def _get_student_mark(self):
        rounded_mark = math.floor(self.__student_mark)
        return rounded_mark

    def __str__(self):
        return f"Student ID: {self.__student_id}, Course: {self.__course_name}, Mark: {self.__student_mark}"    
         

# Input a number of students in an class
def input_student(students_list):
    # Ask the user how many students would they like to add
    while True:
        try:
            no_students = int(input("Input number of students to be added in the class: "))
            if no_students <= 0:
                print("There must be at least one student")
            else:
                break
        except ValueError:
            print("Must be an integer!")

    # Inputting neccessary info for students
    for s in range(0, no_students, 1):
        while True:
            try:
                print(f"---Student {s + 1}. ")
                student_id = str(input("Student ID: "))
                student_name = str(input("Name: "))
                student_dob = str(input("D.O.B (DD/MM/YYYY): "))

                if student_id == "" or student_name == "" or student_dob == "":
                    print("try again")
                    continue
                else:
                    # Check if the student had already existed yet
                    for student_obj in students_list:
                        if student_obj._get_id() == student_id:
                            print("Student already exist!")
                            return
                    
                    # Create a new Student object and append it to the students_list
                    new_student = Student(student_name, student_id, student_dob)
                    students_list.append(new_student)
                    break

            except:
                print("Something went wrong, try again.")

# List out all students in the class
# TODO: Decorate the UI with "curses"
def list_student(students_list):
    print("---List of students in the class---")
    counter = 1
    for student_obj in students_list:
        print(f"Student {counter}. Name: {student_obj._get_name()}, ID: {student_obj._get_id()}, D.O.B: {student_obj._get_dob()}")
        counter = counter + 1

# Input a number of courses
# TODO: Decorate the UI with "curses"
def input_course(course_list):
    # Ask the user how many courses they would like to add
    while True:
        try:
            no_courses = int(input("Input number of courses to be added: "))
            if no_courses <= 0:
                print("There must be at least one course")
            else:
                break
        except ValueError:
            print("Must be an integer!")

    # Inputting neccessary info for the courses
    for c in range(0, no_courses, 1):
        while True:
            print(f"---Course {c + 1}. ")
            course_name = str(input("Course Name: "))
            course_id = str(input("Course ID: "))
            if course_id == "" or course_name == "":
                print("try again")
            else:
                # Check if the course exist yet
                for course_obj in course_list:
                    if course_obj._get_name() == course_name or course_obj._get_id() == course_id:
                        print("Course already exist!")
                        return

                new_course = Course(course_name, course_id)
                course_list.append(new_course)
                break

# List out available courses
# TODO: Decorate the UI with "curses"
def list_course(courses_list):
    counter = 1
    print("---List of courses available---")
    for course_obj in courses_list:
        print(f"Course {counter}. {course_obj._get_name()}, ID: {course_obj._get_id()}")
        counter = counter + 1

# Select a course, input marks for a student in that courses
# TODO: Decorate the UI with "curses"
def input_mark(students_list, courses_list, marks_list):
    student_id = str(input("Student's ID: "))

    student_exist = False
    course_exist = False

    # Check if the student exist 
    if len(students_list) == 0:
        print("Student does not exist!")
        return
    else:
        for student_obj in students_list:
            if student_obj._get_id() == student_id:
                student_exist = True

    course_name = str(input("Course's name: "))

    # Check if the course exist
    if len(courses_list) == 0:
        print("Course does not exist!")
        return
    else:
        for course_obj in courses_list:
            if course_obj._get_name() == course_name:
                course_exist = True

    # If student or course does not exist, then the function stops
    if student_exist == False:
        print("Student does not exist!")
        return
    if course_exist == False:
        print("Course does not exist!")
        return

    # Ask the user the student's mark for that course
    student_mark = 0
    while True:
        try:
            student_mark = float(input("Input mark here: "))
            if student_mark < 0:
                print("Mark must be non-negative")
            elif student_mark > 10:
                print("Mark is too big!")
            else:
                break
        except ValueError:
            print("Mark must be a number!")
    
    # The student mark will be an object
    student_mark_obj = StudentMark(student_id, course_name, student_mark)

    # Add the mark's info into the list
    marks_list.append(student_mark_obj)

# List out all mark of a student
# TODO: Decorate the UI with "curses"
def list_mark(marks_list):    
    search_target = str(input("Enter the student ID: "))

    counter = 0
    for mark_obj in marks_list:
        if mark_obj._get_student_id() == search_target:
            print(f"Course: {mark_obj._get_course_name()}, Mark: {mark_obj._get_student_mark()}")
            counter = counter + 1
            
    #curses.endwin()

# Calculate average GPA of a given student (Done)
# TODO: Decorate the UI with "curses"
# PSEUDOCODE
# step 1: the user type in student's id
# step 2: calculate the average GPA of the student
#       2.1: create a new, empty np (numpy) array
#       2.2: iterate through the student_marks_list list
#       2.3: for every matched student id in the list, append them into the np array
#       2.4: get the marks in each student_mark object and begin calculate average gpa
# step 3: return the average GPA 
def average_gpa(student_id, student_marks_list, courses_list, display_mode=False):

    # Initialize the average gpa variable
    avg_gpa = 0

    # Initialize the max gpa variable
    # this variable exist to display the student's maximum gpa that they could achieve
    max_gpa = 0

    # For every matched student id in the list, append them into the temp_list
    temp_list = []
    for student_mark_object in student_marks_list:
        if student_mark_object._get_student_id() == student_id:
            temp_list.append(student_mark_object._get_student_mark())

    # Create a new np array from temp_list list
    mark_array = np.array(temp_list)

    # Calculating the student's average GPA, as well as their possible max gpa
    for mark in mark_array:
        avg_gpa = avg_gpa + mark
    avg_gpa = avg_gpa / float(len(courses_list))

    for course in courses_list:
        max_gpa = max_gpa + 10
    max_gpa = max_gpa / float(len(courses_list))

    # Display the student's average gpa / max gpa they could achieve
    # if display_mode is set to true
    if display_mode == True:
        print(f"Average GPA: {avg_gpa}/{max_gpa}")
    else: # Simply return the avg_gpa if display_mode is set to false
        return avg_gpa

# TODO: Sort student by descending GPA
# step 1: initiate an empty numpy array
# step 2: for every student in the student_marks_list list, do:
#       2.1. calculate a student's gpa using average_gpa()
#       2.2. append the student's id and their average_gpa into a list
# step 3: sort by descending GPA (Display the student's name associated with the gpas)
def sort_student(student_list, student_marks_list, courses_list):
    
    # For every student in the student_list list, append (student_id, average_gpa of said student) into temp_gpa_list list
    temp_gpa_list = []
    for student in student_list:
        temp_gpa_list.append((student._get_id(),average_gpa(student._get_id(), student_marks_list, courses_list, False)))
    
    # Sort the temp_gpa_list list according to GPA by descending order
    gpa_array = np.array(temp_gpa_list)
    gpa_array = gpa_array[np.argsort(gpa_array[:, 1])]

    # Display the result
    print(f"Student list sorted by descending GPA (Format: Student ID, Average GPA): \n{gpa_array[::-1]}")


# Execute the code
# This code will loop until terminated
# TODO: Decorate the UI using the "curses" module
if __name__ == "__main__":
    print("------Student Mark management system------")
    
    while True:        
        print("---Here are the things that you could do---")
        print("1. Add new student(s)")
        print("2. Add new course(s)")
        print("3. Select a course and input mark for student")
        print("4. List out all students")
        print("5. List out all courses")
        print("6. List out all students' mark for each courses")
        print("7. Average GPA of a student")
        print("8. Sort students by descending GPA")
        print("9. Exit")

        op = input("What do you want to do? (1-9): ")
    
        # Use this code if you're using a Python version 3.10 or later
        match op:
            case "1":
                input_student(students_list)
            case "2":
                input_course(courses_list)
            case "3":
                input_mark(students_list, courses_list, marks_list)
            case "4":
                list_student(students_list)
            case "5":
                list_course(courses_list)
            case "6":
                list_mark(marks_list)
            case "7":
                # Ask the user for the student's ID
                student_id = str(input("Enter the student ID: "))
                average_gpa(student_id, marks_list, courses_list, True)
            case "8":
                sort_student(students_list, marks_list, courses_list)
            case "9":
                exit()
            case _:
                print("Invalid input")

        print("\n")
