class parentclass:
    def parent_function(self):
        print("This is a parent class")

class child_class(parentclass):
    def child_function(self):
        print("This is an child class")

        super().parent_function()


child_obj = child_class()
child_obj.child_function()
