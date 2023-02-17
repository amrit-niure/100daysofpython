# class Employee:
#     def __init__(self):
#         self.__name = "Harry"
# a = Employee()

# # print(a.__name)
# print(a._Employee__name)
# print(a.__dir__())

class student:
    def __init__(self):
        self.name = "harry"

    def _funName(self):
        return "CodeWithHarry"

class subject(student):
    pass

obj = student()
obj1 = subject()
print(dir(obj))

# calling by object of student class 
print(obj.name)
print(obj._funName())

# calling by object of class 
print(obj1.name)
print(obj1._funName())
