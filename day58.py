# class Person:
#     def __init__(self,n,o):
#         print("Hey I am a Person")
#         self.name = n
#         self.occ = o
#     def info(self):
#         print(f"{self.name} is {self.occ}")

# a = Person("Amrit","Developer")
# b = Person("Rohan","Fire Fighter")
# # print(a.name)
# # a.name = "Saru"
# # a.occ = "HR"
# a.info()
# b.info()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.make} {self.model}'s engine has started.")

my_car = Car("Lambo", "Avendure", 2021)
my_car = Car("Toyota", "Camry", 2020)
your_car = Car("Honda","Something",2022)
my_car.start_engine() # Output: The Toyota Camry's engine has started.
your_car.start_engine() # Output: The Toyota Camry's engine has started.
