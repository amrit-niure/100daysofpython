# class MyClass:
#     def __init__(self,value):
#         self._value = value
    
#     def show(self):
#         print(f"value is {self._value}")

#     @property
#     def Ten_value(self):
#         return 10 *self._value
#     @Ten_value.setter
#     def Ten_value(self):
#         return 10 *self._value

# obj = MyClass(10)
# print(obj.Ten_value)
# obj.show()
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

# create a Circle object
c = Circle(5)

# get the radius
print(c.radius) # 5

# set the radius
c.radius = 10

# get the updated radius
print(c.radius) # 10
