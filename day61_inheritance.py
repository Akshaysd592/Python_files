class Employee:
    def __init__(self, name, id):
        self.name= name 
        self.id=id

    def showdetails(self):
        print(f"The name of employee is {self.name} and id is {self.id} ")


class programmer(Employee):
    def showlanguage(self):
        print("The default language is python" )



akshay = Employee("akshay", 5)
akshay.showdetails()
a= programmer("aman", 10)
a.showdetails()
a.showlanguage()

