"""An object is an instance of a class. It represents a real entity and occupies memory.
object has identity, state, behavior ,created using class name

#syntax:
obj = ClassName()

"""
class Book:
    def __init__(self, title):
        self.title = title

b1 = Book("Python")
print(b1.title)
#Here b1 is the object.
