class employee:
   def __init__(self, name):
    self.name = name

   def __str__(self):
     return (f"This is a str function printing {self.name}")
   def __repr__(self):
     return (f"This is a str function printing {self.name} this is repr")

   def __call__ (self):
      print  ("this is object call")