
class Parent:
    def display_parent(self):
        print("This is Parent class")


class Child(Parent):
    def display_child(self):
        print("This is Child class")


obj = Child()
obj.display_parent()
obj.display_child()
