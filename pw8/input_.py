import domains
import time 

# Actually, I'm not going to "curse" this module anymore

def __init__():
    pass

def input_student(students_list):
    """
    Input a number of students in a class

    Parameter
    ----------
    students_list: a list of Student objects

    Return None
    """
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
            time.sleep(1)

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
                    new_student = domains.Student(student_id, student_name, student_dob)
                    students_list.append(new_student)
                    break
            except:
                print("Something went wrong, try again.")

def input_course(course_list):
    """
    Input a number of courses

    Parameter
    ----------
    course_list: a list of Course objects

    Return None
    """
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
            time.sleep(1)

    # Inputting neccessary info for the courses
    for c in range(0, no_courses, 1):
        while True:
            print(f"---Course {c + 1}. ")
            course_id = str(input("Course ID: "))
            course_name = str(input("Course Name: "))
            if course_id == "" or course_name == "":
                print("try again")
            else:
                # Check if the course exist yet
                for course_obj in course_list:
                    if course_obj._get_name() == course_name or course_obj._get_id() == course_id:
                        print("Course already exist!")
                        return
                
                # Create a new Course object and append it to the course_list
                new_course = domains.Course(course_id, course_name)
                course_list.append(new_course)
                break

def input_mark(students_list, courses_list, marks_list):
    """
    Select a course and input mark for a student in that courses

    Parameters
    -----------
    students_list: a list of Student objects
    course_list: a list of Course objects
    marks_list: a list of StudentMark objects

    Return None
    """
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

    course_id = str(input("Course's ID: "))

    # Check if the course exist
    if len(courses_list) == 0:
        print("Course does not exist!")
        return
    else:
        for course_obj in courses_list:
            if course_obj._get_id() == course_id:
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
            time.sleep(1)

    # The student mark will be an object
    student_mark_obj = domains.StudentMark(student_id, course_id, student_mark)

    # Add the mark's info into the list
    marks_list.append(student_mark_obj)

