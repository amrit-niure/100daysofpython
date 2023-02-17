class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The id of Employee : {self.name} is {self.id}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e1 = Employee("Rohan Das", 420)
e1.showDetails()
e2 = Programmer("Amrit",400)
e2.showDetails()
e1.showLanguage()
e2.showLanguage()