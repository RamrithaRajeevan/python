#create class Teacher with name, age, &salary attribute where salary must be private attributes that cannot be accesse outside class.
class Teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary=salary
    def get_salary(self):
       return self.__salary
    def set_salary(self,salary):
      if salary>0:
        self.__salary=salary
      else:
        print("invalid salary")

teacher = Teacher("Reshma", 30, 50000)
print(f"Name: {teacher.name}")
print(f"Age: {teacher.age}")
print(f"Salary: {teacher.get_salary()}")  

teacher.set_salary(55000)  
print(f"Updated Salary: {teacher.get_salary()}")