
# Objectives: 
# • Use math module to round-down student scores to 1-digit decimal upon input, floor() (done)
# • Use numpy module and its array to
#   • Add function to calculate average GPA for a given student (done)
#       • Weighted sum of credits and marks
#   • Sort student list by GPA descending (done)
# • Decorate your UI with curses module (I'll assume that we only need to use curses for output functions,
#       but maybe I'll come back and implement them for input functions as well in the future,
#       also feedback regarding the UI is ok)
# • Push your work to corresponding forked Github repository

import math
import numpy as np

import curses
import curses.textpad

import os

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
# TODO: Decorate the UI with "curses" (later)
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
def list_student(students_list):
    # Initialize the screen
    stdscr = curses.initscr()

    # Temporarily erase the terminal
    stdscr.erase()
    stdscr.addstr(0, 20, "---<List of students in the class>---", curses.A_BOLD)

    # List out all students
    counter = 1
    line = 1
    for student_obj in students_list:
        stdscr.addstr(line + 1, 1, f"-- Student {counter}.")
        stdscr.addstr(line + 2, 4, f"• Name: {student_obj._get_name()}")
        stdscr.addstr(line + 3, 4, f"• ID: {student_obj._get_id()}")
        stdscr.addstr(line + 4, 4, f"• D.O.B: {student_obj._get_dob()}")
        line = line + 5

        counter = counter + 1
    
    # Refresh the screen so that the result show up in the terminal
    stdscr.refresh()

    # Restore the terminal its original state when user type a single key
    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    curses.endwin()

# Input a number of courses
# TODO: Decorate the UI with "curses" (later)
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
def list_course(courses_list):
    # Initialize the screen
    stdscr = curses.initscr()

    # Temporarily erase the terminal
    stdscr.erase()
    stdscr.addstr(0, 20, "---<List of courses available>---", curses.A_BOLD)

    # List out all courses
    counter = 1
    line = 1
    for course_obj in courses_list:
        stdscr.addstr(line + 1, 1, f"-- Course {counter}.")
        stdscr.addstr(line + 2, 4, f"• Name: {course_obj._get_name()}")
        stdscr.addstr(line + 3, 4, f"• ID: {course_obj._get_id()}")
        line = line + 4

        counter = counter + 1
    
    # Refresh the screen so that the result show up in the terminal
    stdscr.refresh()

    # Restore the terminal its original state when user type a single key
    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    curses.endwin()

# Select a course, input marks for a student in that courses
# TODO: Decorate the UI with "curses" (later)
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
def list_mark(marks_list):  
    search_target = str(input("Enter the student ID: "))
    stdscr = curses.initscr()

    # Temporarily erase the terminal
    stdscr.erase()
    stdscr.addstr(0, 20, f"---<List of marks of student {search_target}>---", curses.A_BOLD)

    # List out all courses
    line = 1
    for mark_obj in marks_list:
        if mark_obj._get_student_id() == search_target:
            stdscr.addstr(line + 1, 1, f"-- Course: {mark_obj._get_course_name()}")
            stdscr.addstr(line + 2, 4, f"• Mark: {mark_obj._get_student_mark()}")
            line = line + 3
    
    # Refresh the screen so that the result show up in the terminal
    stdscr.refresh()

    # Restore the terminal its original state when user type a single key
    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    curses.endwin()

# Calculate average GPA of a given student
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

    # Calculating the student's average GPA
    for mark in mark_array:
        avg_gpa = avg_gpa + mark
    avg_gpa = avg_gpa / float(len(courses_list))
    # as well as their possible max gpa
    for course in courses_list:
        max_gpa = max_gpa + 10
    max_gpa = max_gpa / float(len(courses_list))

    # Display the student's average gpa / max gpa they could achieve
    # if display_mode == true
    if display_mode == True:
        stdscr = curses.initscr()
        stdscr.erase()

        # Create a textbox containing the student's average GPA
        curses.textpad.rectangle(stdscr, 2, 2, 5, 60)
        stdscr.addstr(3, 5, f"Average GPA of student with the ID {student_id} is: {avg_gpa}/{max_gpa}")
        stdscr.refresh()
        
        # Restore the terminal's original state after the user press a key
        stdscr.addstr(12, 0, "\nPress any key to continue...", curses.A_BOLD)
        stdscr.getch()
        curses.endwin()
    else: # Simply return the avg_gpa variable if display_mode == false
        return avg_gpa

# Sort student by descending GPA
def sort_student(student_list, student_marks_list, courses_list):
    # Initialize a new screen
    stdscr = curses.initscr()
    stdscr.erase()

    # For every student in the student_list list, append (student_id, average_gpa of said student) into temp_gpa_list list
    temp_gpa_list = []
    for student in student_list:
        temp_gpa_list.append((student._get_id(),average_gpa(student._get_id(), student_marks_list, courses_list, False)))
    
    # Create a new array from temp_gpa_list
    gpa_array = np.array(temp_gpa_list)
    # Sort the temp_gpa_list list according to GPA by descending order
    gpa_array = reversed(gpa_array[np.argsort(gpa_array[:, 1])])

    # Display the result
    stdscr.addstr(1, 20, "---<List of student by descending GPA>---", curses.A_BOLD)
    line = 4
    for gpa in gpa_array:
        stdscr.addstr(line, 4, f"• Student ID: {gpa[0]}, GPA: {gpa[1]}")
        line += 1
    stdscr.refresh()

    # Restore the terminal's original state after the user press a key
    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    curses.endwin()


# Execute the code
# This code will loop until terminated
def main():
    student_1 = Student("tung", "1", "1")
    student_2 = Student("le", "2", "2")
    student_3 = Student("lemao", "3", "3")

    students_list.append(student_1)
    students_list.append(student_2)
    students_list.append(student_3)

    course_1 = Course("math", "1c")
    course_2 = Course("python", "2c")

    courses_list.append(course_1)
    courses_list.append(course_2)

    student_1_mark_1 = StudentMark("1", "math", 9.45)
    student_1_mark_2 = StudentMark("1", "python", 7.5)
    student_2_mark_1 = StudentMark("2", "math", 10)
    student_2_mark_2 = StudentMark("2", "python", 5)
    student_3_mark_1 = StudentMark("3", "math", 8)
    student_3_mark_2 = StudentMark("3", "python", 9)

    marks_list.append(student_1_mark_1)
    marks_list.append(student_1_mark_2)
    marks_list.append(student_2_mark_1)
    marks_list.append(student_2_mark_2)
    marks_list.append(student_3_mark_1)
    marks_list.append(student_3_mark_2)

    while True:      
        os.system('clear')

        print("------Student Mark management system------")
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

main()
#curses.wrapper(main)