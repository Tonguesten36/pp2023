import subprocess
import os
import curses

import tarfile as tar
import os.path as path

import output as out
import input_ as inp
import load_data as ld

# • Copy your pw4 directory into pw5 directory (done)

# • Update your input functions (done)
#   • Write student info to students.txt after finishing input (done)
#   • Write course info to courses.txt after finishing input (done)
#   • Write marks to marks.txt after finishing input (done)

# • Before closing your program
#   • Select a compression method (I'll use gzip for this one)
#   • Compress all files aboves into students.dat (actually, it should be students.tar.gz instead) (done)
#       Step 1: use tarfile to combine all data in students.txt, courses.txt, marks.txt into a tar file (done)
#       Step 2: compress the tar file with gzip   (done)

# • Upon starting your program,
#   • Check if students.dat exists (again, it should be students.tar.gz instead) (done)
#   • If yes, decompress and load data from it

# • Push your work to corresponding forked Github repository

# Data
students_list = []
courses_list = []
marks_list = []
save_files = ["students.txt", "courses.txt", "marks.txt"]

# If students.tar.gz does not exist then we create new savefiles
def check_if_savefiles_not_exists(file_names):
    if path.exists("students.tar.gz") == False:
        for i in range(0, 3, 1):
            # Create a new file with specific name if it does not exist yet
            if path.exists(file_names[i]) == False:
                new_file = open(file_names[i], 'x')
                new_file.close()

# Combine all data into a tar.gz file
def combine_all_to_tarfile(file_names):
    # create a new student.tar.gz file if it does not exist yet
    if path.exists("students.tar.gz") == False:
        new_tar_file = tar.open("students.tar.gz", "x:gz")
        new_tar_file.close()

    # Combine all three .txt files into a single tar.gz file
    with tar.open("students.tar.gz", "w:gz") as students_tar:
        for name in file_names:
            students_tar.add(name) 
            os.remove(name)

# Extract all data from students.tar.gz
def extract_tarfile(file_names):
    # Clean up any .txt files lingering in the directory
    for file in file_names:
        if path.exists(file):
            os.remove(file)

    # Check if the .tar.gz file exist
    if path.exists("students.tar.gz"):
        try:
            # Open the .tar.gz file and extract all data inside it
            # Once finished, the program will delete the .tar.gz file
            student_tar = tar.open("students.tar.gz", "r:gz")
            for name in file_names:
                student_tar.extract(name)
            student_tar.close()
            os.remove("students.tar.gz")

            # Load all data from students.tar.gz into students_list, courses_list and marks_list
            ld.load_data(file_names[0], students_list, 's')
            ld.load_data(file_names[1], courses_list, 'c')
            ld.load_data(file_names[2], marks_list, 'm')
            return True
        except tar.ExtractError:
            return False

# Execute the code
# This code will loop until terminated
def main():

    # Check if the save files (students.txt, courses.txt, marks.txt) exist yet
    # If not then create these files
    check_if_savefiles_not_exists(save_files)

    # Extrall all data from students.tar.gz
    extract_tarfile(save_files)
    
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
                # Sort the students by descending GPA scores
                out.sort_student(students_list, marks_list, courses_list)
            case "9":    
                # Save all data into a tar.gz file before exit the program
                combine_all_to_tarfile(save_files)
                exit()
            case _:
                print("Invalid input")

# Run the code
main()