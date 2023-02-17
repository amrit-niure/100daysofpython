class Person:
    name = "Amrit"
    occupation = "Software Developer"
    age = 20 
    worth = 100
    def info(self):
        print(f"{self.name} is {self.occupation}")

a = Person()
b = Person()
# a.name = "Subham"
# a.occupation = "Fire fighter"
b.name = "Harry"
b.occupation = "Software Engineer"
# print(a.name)
a.info()
b.info()
