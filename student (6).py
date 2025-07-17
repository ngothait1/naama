from person import Person
from utils import parse_valid_int

class Student(Person):
    def __init__(self, _id, name, age):
        super().__init__(_id, name, age)

        msg = "Error: Invalid input!"
        self._field_of_study = input("Field of study: ")
        
        year_input = input("Year of study: ")
        self._year_of_study = parse_valid_int(year_input)
        if self._year_of_study is None:
            raise ValueError(msg)
        
        grade_input = input("Grade average: ")
        self._grade_average = parse_valid_int(grade_input)
        if self._grade_average is None:
            raise ValueError(msg)

    def get_field_of_study(self):
        return self._field_of_study
    
    def get_year_of_study(self):
        return self._year_of_study

    def get_grade_average(self):
        return self._grade_average
    
    def __str__(self):
        person_info = super().__str__()
        return f"{person_info} Student in year {self.get_year_of_study()} studying {self.get_field_of_study()}. Average grade: {self.get_grade_average()}."
    
    def print_myself(self):
        print(self)

    def to_dict(self):
        user_data = super().to_dict()
        user_data.update({
            "Field of study": self.get_field_of_study(),
            "Year of study" : self.get_year_of_study(),
            "Average grade" : self.get_grade_average()
        })
        return user_data

    


