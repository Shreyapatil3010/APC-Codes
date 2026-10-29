
class A:
    def show_a(self):
        print("This is class A")


class B(A):
    def show_b(self):
        print("This is class B")


class C(A):
    def show_c(self):
        print("This is class C")


class D(B, C):
    def show_d(self):
        print("This is class D")


obj = D()
obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()
