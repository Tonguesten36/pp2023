import subprocess
import output as out
import input_ as inp

# Data
students_list = []
courses_list = []
marks_list = []

# Execute the code
# This code will loop until terminated
def main():
    while True:
        subprocess.run(["clear"])

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
                inp.input_student(students_list)
            case "2":
                inp.input_course(courses_list)
            case "3":
                inp.input_mark(students_list, courses_list, marks_list)
            case "4":
                out.list_student(students_list)
            case "5":
                out.list_course(courses_list)
            case "6":
                out.list_mark(marks_list)
            case "7":
                # Ask the user for the student's ID
                student_id = str(input("Enter the student ID: "))
                out.average_gpa(student_id, marks_list, courses_list, True)
            case "8":
                out.sort_student(students_list, marks_list, courses_list)
            case "9":
                exit()
            case _:
                print("Invalid input")

main()