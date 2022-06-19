class ParentClass:
    def print_msg(self):
        print("Parent msg")

class ChildClass(ParentClass):
    def print_msg(self):
        print("Child msg")

class ChildClass2(ParentClass):
    def print_msg(self):
        super().print_msg()
        print("Child2 msg")

obj_1 = ChildClass()
obj_2 = ChildClass2()

obj_1.print_msg()
obj_2.print_msg()
