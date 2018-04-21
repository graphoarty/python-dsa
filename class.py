# A class for the person
# self is a reference to the object you have created
class Person():

    # The constructor that gets called when you create a new object
    def __init__(self, name):
        self.name = name

    def get_name(self,s):
        return s.name

# Creating a new object Person and storing the reference in aditya
aditya = Person(name="Aditya Joshi")
quinston = Person(name="Quinston Pimenta")
suraj = Person(name="Suraj Saste")

print(aditya.get_name(aditya))
print(quinston.get_name(quinston))
print(suraj.get_name(suraj))