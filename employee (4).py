from person import Person
from utils import parse_valid_int

class Employee(Person):
    def __init__(self, _id, name, age):
        super().__init__(_id, name, age)

        self._field_of_work = input("Field of work: ")

        salary_input = input("Salary: ")
        self._salary = parse_valid_int(salary_input)
        if self._salary is None:
            raise ValueError("Error: Invalid input for salary!")

    def get_field_of_work(self):
        return self._field_of_work
    
    def get_salary(self):
        return self._salary
    
    def __str__(self):
        person_info = super().__str__()
        return f"{person_info} Works in {self.get_field_of_work()}, earning {self.get_salary()}."
    
    def print_myself(self):
        print(self)

    def to_dict(self):
        user_data = super().to_dict()
        user_data.update({
            "Field of work": self.get_field_of_work(),
            "Salary": self.get_salary()
        })
        return user_data



