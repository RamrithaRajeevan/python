#program to create person class. Include attributes like name, country& DOB. Implement method to determine person age.

from datetime import datetime
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def calculate_age(self):
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age

person = Person("Riya", "India", "1992-05-12")
print(f"Name: {person.name}")
print(f"Country: {person.country}")
print(f"Date of Birth: {person.dob}")
print(f"Age: {person.calculate_age()}")
        