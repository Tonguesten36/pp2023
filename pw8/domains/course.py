from .object import Object

def __init__():
    pass

class Course(Object):
    def __init__(self, id, name):
        super().__init__(id, name)
    
    def __str__(self):
        return super().__str__()

    def __lt__(self, other_course):
        return self._id == other_course._id