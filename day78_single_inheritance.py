class Animal : 
 def __init__(self, name, species) :
  self.name = name
  self.species = species
  
 def make_sound(self):
    print("this animal can make sound")

class dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="dog")
        self.breed = breed

    def make_sound(self):
        print("bark")

A = dog("dog","dogerman")
A.make_sound()
print(A.species)
print(A.breed)


b = Animal("dog","dog")
b.make_sound()
print(b.species)