'''
---method overloading, multiple methods can have the same name with different parameters---
Declaring a method in the subclass which already exists there in the parent class is known as method overriding.
When a class is inheriting a method from a superclass of its own,
then there is an option of overriding the method provided it is not declared as final.

Function overriding is a feature that allows us to have a same function in child class which is already present in the parent class.
A child class inherits the data members and member functions of parent class,
but when you want to override a functionality in the child class then you can use function overriding.
'''

#for example-

class Person:
    def job(self):
        print(" i can do anything")

class Teacher(Person):
    def job(self):
        print("I AM TEACHER")

class Student(Person):
    def job(self):
        print("I AM STUDENT")


Student_object = Student()
Student_object.job() #kono parameter na thakle method k call korar somoy () dete hobe.

Teacher_object = Teacher()
Teacher_object.job()