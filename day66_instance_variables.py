class employee:
    company = "Apple"
    numberofemployee = 0 
    def __init__(self, name) :
        self.name  = name
        self.raise_amount = 0.32
        employee.numberofemployee += 1
    
    def showdata(self):
        print(f"The name of employee is  {self.name} and raised amount in { self.numberofemployee} sized  company { self.company} is { self.raise_amount}")





employee.company= "Google"  #here changing company name to google for employee class 
emp1 = employee("Akshay")

emp1.showdata()
# employee.showdata(emp1)
emp2= employee("Sanket")
emp2.raise_amount = 0.444

emp2.company = "meta" # here overiding value of google by meta  called instance variables 
emp2.showdata()


