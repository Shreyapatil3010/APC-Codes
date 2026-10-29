
class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called")
        print("Student Name:", self.name)

    def __del__(self):
        print("Destructor called")
        print("Object destroyed")


s1 = Student("Shreya")
del s1
