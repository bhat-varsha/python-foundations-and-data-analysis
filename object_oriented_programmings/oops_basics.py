"""
Object-Oriented Programming (OOP) is a programming approach in
which a program is organized around objects that contain data (attributes) and functions (methods).

"""
student_name="varsha"
age=22
marks=85

def is_pass(marks):
    return marks>35
print(is_pass(marks))
#if this prgrm we have to do for many students then it will be difficult
#object_oriented_programmings main goal is Keep data and the actions that work on that data together.
"""
❌ Without OOP
student_name
student_age
student_marks
is_pass(student_marks)
calculate_grade(student_marks)
        (Everything is scattered.)

✅ With OOP (idea only)
Student
 ├── name
 ├── age
 ├── marks
 ├── is_pass()
 └── calculate_grade()
        (Everything related to Student stays together.)
        
(advantages)
Code reuse (using inheritance)
Easy to manage large programs
Security / data hiding (encapsulation)
Real-world modeling (Student, BankAccount, DNASequence etc.)
"""
#syntax:
class ClassName:
    def __init__(self):
        ...
    def method(self):
        ...
obj = ClassName()
obj.method()

#example:
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(self.name, self.roll)

s1 = Student("Varsha", 101)
s1.display()


