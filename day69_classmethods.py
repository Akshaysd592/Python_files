class employee:
    company = "google"

    def show(self):
        print(f"The company name is  {self.company} and employee name is {self.name}")


    @classmethod #used to make changes in original class value 
    def assign (a,company): # here a is taking object and company is taking a value of company to be assigned
        a.company = company 


a = employee()

a.name = "Akshay"
a.show()
a.assign("instagram")
a.show()

print(employee.company) #classfunction in class  used to change original variable value in class 

