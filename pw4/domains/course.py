from .object import Object

def __init__():
    pass

class Course(Object):
    def __init__(self, name, id):
        super().__init__(name, id)
    
    def __str__(self):
        return super().__str__()

    def __lt__(self, other_course):
        return (self._name == other_course._name) or (self._id == other_course._id)