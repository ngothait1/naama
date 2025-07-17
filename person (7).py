
class Person:
    def __init__(self, _id, name, age):
        self._id = _id
        self._name = name
        self._age = age

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def __str__(self):
        return f"{self._name} ID: {self._id}, is {self._age} years old."
    
    def print_myself(self):
        print(self)

    def to_dict(self):
        return {
            "Id": self.get_id(),
            "Name": self.get_name(),
            "Age": self.get_age()
        }

    
