
# Student mark management system, with tuples, dicts, lists
# Functions include:
#   Input function
#       • Input a number of students in a class (a list of student dictionaries) (done)
#       • Input student info: id, name, dob (dictionary)
#       • Input number of courses (a list of courses dictionaries)
#       • Input course info: id, name (dictionary)
#       • Select a course, input mark for students in this course
#   Listing functions:
#       • List courses
#       • List students
#       • Show student marks for a given course

# The input function
def input_func():
    # Number of students
    no_students = 0
    # Number of courses
    no_courses = 0

    # Lists of students
    student_list = []
    # Lists of courses 
    course_list = []
    # Lists of students' marks in courses
    student_mark_list = []

    # Input number of students in the class, force the user to input again if the input is invalid
    while True:
        try:
            no_students = int(input("Input number of students in the class: "))
            if no_students <= 0:
                print("There must be at least one student")
            else:
                break
        except:
            print("Must be an integer!")
    
    # Input number of courses, force the user to input again if the input is invalid
    while True:
        try:
            no_courses = int(input("Input number of courses: "))
            if no_courses <= 0:
                print("There must be at least one course")
            else:
                break
        except:
            print("Must be an integer!")
    
    # Input student info: id, name, dob (dictionary)
    print("-----Students-----")
    for s in range(0, no_students, 1):
        while True:
            try:
                student = {}
                student_id = int(input("Student ID: "))
                student_name = str(input("Name: "))
                student_dob = str(input("D.O.B (DD/MM/YYYY): "))
                if student_id <= 0 or student_name == "" or student_dob == "":
                    print("try again")
                else:
                    student.update({"id":student_id})
                    student.update({"name":student_name})
                    student.update({"dob":student_dob})

                    student_list.append(student)
                    break
            except:
                print("Something went wrong, try again.")

    # Input course info: course name, id
    print("-----Courses-----")
    for c in range(0, no_courses, 1):
        while True:
            try:
                course = {}
                course_name = str(input("Course Name: "))
                course_id = int(input("Course ID: "))
                if course_id <= 0 or course_name == "":
                    print("try again")
                else:
                    course.update({"name":course_name})
                    course.update({"id":course_id})

                    course_list.append(course)
                    break
            except:
                print("Something went wrong, try again.")

    # Select a student, input marks for that student in every courses
    print("-----Marks-----")
    for student_dict in student_list:
        for course_dict in course_list:
            # Create a new, empty dict
            mark_for_each_course = {}
            while True:
                try:
                    # Ask the user for the student's mark in a course
                    # Had to put student.get("name") and course.get("name") in separate variables
                    # in order to avoid SyntaxError
                    name_student = student_dict.get("name")
                    name_course = course_dict.get("name")
                    mark = float(input(f"Mark for student {name_student} in {name_course} is: "))
                    
                    # This line of code will return a SyntaxError because of the string "name"
                    # mark = int(input(f"Mark for student {student.get("name")} in {course.get("name")} is: "))

                    # Update the mark_for_each_course dict 
                    mark_for_each_course.update({"student_name":student["name"]})
                    mark_for_each_course.update({"course_name":course["name"]})
                    mark_for_each_course.update({"mark":mark})

                    student_mark_list.append(mark_for_each_course)
                    break
                except:
                    print("Something went wrong, try again.")
    # Return a list of students, a list of courses available, and a list of students' marks in courses
    return student_list, course_list, student_mark_list

# Display list of students, list of courses, and list of students' marks in the courses
def listing_func(students_list, courses_list, marks_list):
    # List out the students
    counter = 1
    print("---List of students in the class---")
    for student_dict in students_list:
        if "name" and "id" and "dob" in student_dict:
            student_name = student_dict.get("name")
            student_id = student_dict.get("id")
            student_dob = student_dict.get("dob")

            print(f"Student {counter}. Name: {student_name}, ID: {student_id}, D.O.B: {student_dob}")
            counter = counter + 1
    
    # List out the courses 
    counter = 1
    print("---List of courses available---")
    for course_dict in courses_list:
        if "name" and "id" in course_dict:
            course_name = course_dict.get("name")
            course_id = course_dict.get("id")

            print(f"Course {counter}. Name: {course_name}, ID: {course_id}")
            counter = counter + 1


# Execute the code
print("---Student Mark management system---")
(students, courses, marks) = input_func()
listing_func(students, courses, marks)

