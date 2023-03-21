import curses
import curses.textpad
import numpy as np

def __init__():
    pass

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
        try:    
            stdscr.addstr(line + 1, 1, f"-- Student {counter}.")
            stdscr.addstr(line + 2, 4, f"• Name: {student_obj._get_name()}")
            stdscr.addstr(line + 3, 4, f"• ID: {student_obj._get_id()}")
            stdscr.addstr(line + 4, 4, f"• D.O.B: {student_obj._get_dob()}")
            line = line + 5

            counter = counter + 1
        except:
            curses.endwin()
            return

    # Refresh the screen so that the result show up in the terminal
    stdscr.refresh()

    # Restore the terminal its original state when user type a single key
    stdscr.addstr(line, 0, "\nPress any key to continue...", curses.A_BOLD)
    stdscr.getch()
    curses.endwin()

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
            stdscr.addstr(line + 1, 1, f"-- Course ID: {mark_obj._get_course_id()}")
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
    try:
        for mark in mark_array:
            avg_gpa = avg_gpa + mark
        avg_gpa = avg_gpa / float(len(courses_list))
        # as well as their possible max gpa
        for course in courses_list:
            max_gpa = max_gpa + 10
        max_gpa = max_gpa / float(len(courses_list))
    except ZeroDivisionError:
        curses.endwin()
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