class Student:
    school:"Akirachix"
    def __init__(self,first_name,last_name,age,country,code):
        self.first_name =first_name
        self.last_name=last_name
        self.age=age
        self.country=country
        self.code=code
    def greeting(self):
        greeting=f"Hello{self.first_name} welcome to {self.school}. Your code is {self.code}"
        return greeting
    
    def greet_student_year_of_birth(self):
        greet=f"Hello {self.first_name} you are {2024-self.age}"
        return greet
    def student_initials(self):
        student_initials=f" your initials are {self.first_name[0]}{self.last_name[0]}"
        return student_initials

    def full_name(self)
         full_name=f"your names are{self.first_name}{self.last_name}"
         return first_name

    def student_enroll(self):
        enrollment=f"Hello {self.first_name}{self.last_name} you have been selected to join {self.school}"  
        return enrollment    

     
