def __init__():
    pass

class Object:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    
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
        return f"ID: {self._id}, Name: {self._name}"