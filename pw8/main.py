import subprocess
import threading

import output as out
import input_ as inp
import compression as comp

# Data
students_list = []
courses_list = []
marks_list = []
save_files = ["students", "courses", "marks"]

# TODO: GO TO compression.py and see what you need to do

# Execute the code
# This code will loop until terminated
def main():
    # Check if the save files (students, courses, marks) exist yet
    # If not then create these files, unless students.tar.gz already exists
    check_savefiles_thread = threading.Thread(target=comp.check_if_savefiles_not_exists, args=(save_files))
    check_savefiles_thread.start()

    # Extrall all data from students.tar.gz
    extract_tarfile_thread = threading.Thread(target=comp.extract_tarfile, args=("students.tar.gz", save_files, students_list, courses_list, marks_list))
    extract_tarfile_thread.start()

    while True:
        # Clear the terminal
        subprocess.run(["clear"])

        # I don't know why I did not use multiline string instead of this monstrosity, but whatever...
        # It still works anyway
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

        # op is used to command the program to do a specific task
        # It takes input from user keyboard
        op = input("What do you want to do? (1-9): ")
        
        # Use this code if you're using a Python version 3.10 or later
        # match op:
        #     case "1":
        #         inp.input_student(students_list)
        #     case "2":
        #         inp.input_course(courses_list)
        #     case "3":
        #         inp.input_mark(students_list, courses_list, marks_list)
        #     case "4":
        #         out.list_student(students_list)
        #     case "5":
        #         out.list_course(courses_list)
        #     case "6":
        #         out.list_mark(marks_list)
        #     case "7":
        #         # Ask the user for the student's ID
        #         student_id = str(input("Enter the student ID: "))
        #         out.average_gpa(student_id, marks_list, courses_list, True)
        #     case "8":
        #         # Sort the students by descending GPA scores
        #         out.sort_student(students_list, marks_list, courses_list)
        #     case "9":    
        #         # Serialize all before exit the program
        #         serialize_students = threading.Thread(target=comp.serialize_objects, args=(students_list, save_files[0]))
        #         serialize_courses = threading.Thread(target=comp.serialize_objects, args=(courses_list, save_files[1]))
        #         serialize_marks = threading.Thread(target=comp.serialize_objects, args=(marks_list, save_files[2]))

        #         # Start the data serializing process
        #         serialize_students.start()
        #         serialize_courses.start()
        #         serialize_marks.start()

        #         # Combine all serialized data into a .tar.gz file before exiting
        #         comp.combine_all_to_tarfile(save_files)
        #         exit()
        #     case _:
        #         print("Invalid input")

        # Use this code if you're using versions earlier than Python 3.10
        if op == "1":
            inp.input_student(students_list)
        elif op == "2":
            inp.input_course(courses_list)
        elif op == "3":
            inp.input_mark(students_list, courses_list, marks_list)
        elif op == "4":
            out.list_student(students_list)
        elif op == "5":
            out.list_course(courses_list)
        elif op == "6":
            out.list_mark(marks_list)
        elif op == "7":
            # Ask the user for the student's ID
            student_id = str(input("Enter the student ID: "))
            out.average_gpa(student_id, marks_list, courses_list, True)
        elif op == "8":
            # Sort the students by descending GPA scores
            out.sort_student(students_list, marks_list, courses_list)
        elif op == "9":
            # Create threads for serializing all data before exit the program
            serialize_students = threading.Thread(target=comp.serialize_objects, args=(students_list, save_files[0]))
            serialize_courses = threading.Thread(target=comp.serialize_objects, args=(courses_list, save_files[1]))
            serialize_marks = threading.Thread(target=comp.serialize_objects, args=(marks_list, save_files[2]))

            # Start the data serializing process
            serialize_students.start()
            serialize_courses.start()
            serialize_marks.start()

            # Combine all serialized data into a .tar.gz file before exiting
            comp.combine_all_to_tarfile(save_files)
            exit()
        else:
            print("Invalid input")


# Run the code
main()