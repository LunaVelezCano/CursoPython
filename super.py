class person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("hola soy una persona")
        
class Student(person):
    def __init__ (self, name, age, student_Id):  
         super().__init__(name, age)
         self.student_Id = student_Id

    def greet(self):
        super().greet()
        print(f"hola mi id de estudiante es {self.student_Id}") 

student = Student ("ana", 20, "12345")

student.greet()