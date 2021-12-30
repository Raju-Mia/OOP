#polyorphism means
'''Polymorphism in Python is the ability of an object to take many forms.
In simple words, polymorphism allows us to perform the same action in many different ways.
Polymorphism means multiple forms. In python we can find the same operator or function taking multiple forms.
It also useful in creating different classes which will have class methods with same name.'''

class Person:
    def __init__(self, name):
        self.Name = name

    def job(self):
        pass

class Teacher(Person):
    def job(self):
        print("MY NAME IS ", self.Name, "I AM TEACHER")

class Student(Person):
    def job(self):
        print("MY NAME IS ", self.Name, "I AM STUDENT")

class Employye(Person):
    def job(self):
        print("MY NAME IS", self.Name, "I AM EMPLOYYE")


Teacher_object = Teacher("RAJU MIA")
Teacher_object.job()

Student_object = Student("ASIF SHIKDER")
Student_object.job()

Employye_object = Employye("JAKIR AHMED")
Employye_object.job()
