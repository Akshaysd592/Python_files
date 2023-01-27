class student:
    def __init__(self,n,o) :
        print("constructor called")
        self.name = n
        self.occ = o


    def func(self):
        print(f"{self.name} is  a {self.occ}")


a = student("Akshay","software developer")
print(a.name, a.occ)
a.func()
# b= student("Ram","UX designer")
b= student(1,2)
print(b.name, b.occ)
b.func()