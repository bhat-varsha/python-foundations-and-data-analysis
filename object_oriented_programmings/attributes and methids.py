#Attributes :Attributes are variables/data stored inside an object.
"""self.name
self.seq
self.roll
"""
#example of two types of attributes:
class Student:
    college = "ABC College"
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("hello")

obj = Student("varsha")
print(obj.name)
obj.hello()
#Methods : A method is a function defined inside a class that describes the behavior of object.
class Student:
    def display(self):
        print("Hello")

obj=Student()
obj.display()
