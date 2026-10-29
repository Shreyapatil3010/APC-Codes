
class Grandparent:
    def __init__(self):
        self.__private_var = "Private variable"
        self._protected_var = "Protected variable"

    def __private_function(self):
        print("This is a private function")

    def _protected_function(self):
        print("This is a protected function")

    def show_private(self):
        print(self.__private_var)
        self.__private_function()


class Parent(Grandparent):
    def display(self):
        print(self._protected_var)
        self._protected_function()


class Child(Parent):
    def show(self):
        print("Child class accessing protected members")
        print(self._protected_var)
        self._protected_function()


obj = Child()

obj.show_private()
obj.display()
obj.show()
