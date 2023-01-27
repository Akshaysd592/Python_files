class student():
    name="Akshay"
    mark=int(98)
    def info(self):
        print(f"{self.name} having obtained marks are {self.mark}" )

a  = student()
# a.name= "Sanket"
# a.mark= 99
print(a.name, a.mark)
a.info()