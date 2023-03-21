import math

def __init__():
    pass

class StudentMark:
    def __init__(self, student_id, course_id, mark):
        self.__student_id = student_id
        self.__course_id = course_id
        self.__student_mark = mark
    
    def _get_course_id(self):
        return self.__course_id

    def _get_student_id(self):
        return self.__student_id
    
    def _get_student_mark(self):
        rounded_mark = math.floor(self.__student_mark)
        return rounded_mark

    def __str__(self):
        return f"Student ID: {self.__student_id}, Course: {self.__course_id}, Mark: {self.__student_mark}"   