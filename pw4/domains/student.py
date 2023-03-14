from .object import Object

def __init__():
    pass

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