
# Objective: OOP-fy 1.student.mark.py
# Students, Courses, StudentMarks should be an object

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

    def __str__(self):
        return f"Name: {self._name}, ID: {self._id}, D.O.B: {self.__student_dob}"
    
class Course(Object):
    def __init__(self, name, id):
        super().__init__(name, id)
    
    def __str__(self):
        return f"Name: {self._name}, ID: {self._id}"

    def __lt__(self, other_course):
        return (self._name == other_course._name) or (self._id == other_course._id)

class StudentMark:
    def __init__(self, student, course, mark):
        self.__student_name = student
        self.__course_name = course
        self.__student_mark = mark
    
    def __str__(self):
        return f"Student: {self.__student_name}, Course: {self.__course_name}, Mark: {self.__student_mark}"    
         

# Input a number of students in an class (done)
def input_student(students_list):
    # Ask the user how many students would they like to add
    while True:
        try:
            no_students = int(input("Input number of students to be added in the class: "))
            if no_students <= 0:
                print("There must be at least one student")
            else:
                break
        except:
            print("Must be an integer!")

    # Inputting neccessary info for students
    for s in range(0, no_students, 1):
        while True:
            try:
                print(f"---Student {s}. ")
                student_id = int(input("Student ID: "))
                student_name = str(input("Name: "))
                student_dob = str(input("D.O.B (DD/MM/YYYY): "))

                if student_id <= 0 or student_name == "" or student_dob == "":
                    print("try again")
                else:
                    # Check if the student exist yet
                    # In the first assignment, the program also check for name
                    # However, I removed that option because I realized that two (or more) students
                    # can have the same name, but not having the same ID
                    for student in students_list:
                        _id = student.get("id")
                        if student_id == _id:
                            print("Student already exist!")
                            return

                    new_student = Student(student_name, student_id, student_dob)

                    students_list.append(new_student)
                    break
            except:
                print("Something went wrong, try again.")

# List out all students in the class (Done)
def list_student(students_list):
    print("---List of students in the class---")
    counter = 1
    for student_obj in students_list:
        print(f"Student {counter}. Name: {student_obj._get_name()}, ID: {student_obj._get_id()}, D.O.B: {student_obj._get_dob()}")
        counter = counter + 1

# Input a number of courses (Done)
def input_course(course_list):
    # Ask the user how many courses they would like to add
    while True:
        try:
            no_courses = int(input("Input number of courses to be added: "))
            if no_courses <= 0:
                print("There must be at least one course")
            else:
                break
        except:
            print("Must be an integer!")

    # Inputting neccessary info for the courses
    for c in range(0, no_courses, 1):
        while True:
            try:
                print(f"---Course {c}. ")
                course_name = str(input("Course Name: "))
                course_id = int(input("Course ID: "))
                if course_id <= 0 or course_name == "":
                    print("try again")
                else:
                    # Check if the course exist yet
                    for course in course_list:
                        name = course.get("name")
                        _id = course.get("id")
                        if course_name == name or course_id == _id:
                            print("Course already exist!")
                            return

                    new_course = Course(name, _id)
                    course_list.append(new_course)
                    break
            except:
                print("Something went wrong, try again.")

# List out available courses (Done)
def list_course(courses_list):
    counter = 1
    print("---List of courses available---")
    for course_dict in courses_list:
        if "name" and "id" in course_dict:
            course_name = course_dict.get("name")
            course_id = course_dict.get("id")

            print(f"Course {counter}. Name: {course_name}, ID: {course_id}")
            counter = counter + 1

# Select a course, input marks for a student in that courses
def input_mark(students_list, courses_list, marks_list):
    student_name = input("Student's name: ")

    # Check if the student exist 
    if len(students_list) == 0:
        print("Student does not exist!")
        return
    else:
        for student_dict in students_list:
            name = student_dict.get("name")
            if student_name != name:
                print("Student does not exist!")
                return
    
    course_name = input("Course's name: ")

    # Check if the course exist
    if len(courses_list) == 0:
        print("Course does not exist!")
        return
    for course_dict in courses_list:
        name = course_dict.get("name")
        if course_name != name or len(courses_list) == 0:
            print("Courses does not exist!")
            return
    
    # Ask the user the student's mark for that course
    student_mark = 0
    while True:
        try:
            student_mark = float(input("Input mark here: "))
            if student_mark < 0:
                print("Mark must be non-negative")
            else:
                break
        except:
            print("Must be a number!")
    
    # The student mark will be a dictionary
    student_mark_dict = {}
    student_mark_dict.update({"student_name":student_name})
    student_mark_dict.update({"course_name":course_name})
    student_mark_dict.update({"student_mark":student_mark})

    # Add the mark's info into the list
    marks_list.append(student_mark_dict)

# List out all mark of a student
def list_mark(marks_list):
    search_target = input("Whose mark do you want to see?: ")

    for mark_dict in marks_list:
        if "student_name" and "course_name" and "student_mark" in mark_dict:
            student_name = mark_dict.get("student_name")
            course_name = mark_dict.get("course_name")
            student_mark = mark_dict.get("student_mark")

            # Display the mark of a specific student
            if search_target == student_name:
                print(f"Student: {student_name}, Course: {course_name}, Mark: {student_mark}")

# Execute the code
# This code will loop until terminated
if __name__ == "__main__":
    print("------Student Mark management system------")

    students_list = []
    courses_list = []
    marks_list = []

    # while True:
    #     print("---Here are the things that you could do---")
    #     print("1. Add new student(s)")
    #     print("2. Add new course(s)")
    #     print("3. Select a course and input mark for student")
    #     print("4. List out all students")
    #     print("5. List out all courses")
    #     print("6. List out all students' mark for each courses")
    #     print("7. Exit")
        
    #     op = input("What do you want to do? (1-7): ")

    student = Student("Name", 1900, "10/06/2003")
    # print(student._get_name())
    # print(student._get_id())
    # print(student)

    course = Course("Meth", 2005)
    # print(course._get_name())
    # print(course._get_id())
    # print(course)
        # Use this code if you're using a Python version 3.10 or later
        # match op:
        #     case "1":
        #         input_student(students_list)
        #     case "2":
        #         input_course(courses_list)
        #     case "3":
        #         input_mark(students_list, courses_list, marks_list)
        #     case "4":
        #         list_student(students_list)
        #     case "5":
        #         list_course(courses_list)
        #     case "6":
        #         list_mark(marks_list)
        #     case "7":
        #         exit()
        #     case _:
        #         print("Invalid input")

    print("\n")
