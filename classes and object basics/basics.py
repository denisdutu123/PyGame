# definition of a class
class person():
    # attributes
    name = "Denis"
    height = 185
    shoesize = 42
    city = "New York"
    #constructor
    def __init__(self):
        print("object is created")

    #behaviour 
    def info(self):
        self.name = input("Enter your name")
        self.height = input("Enter your height")
        self.shoesize = input("Enter your shoesize")
        self.city = input("Enter your city")
    def out(self):
        print("Name is:",self.name)
        print("Height is:",self.height)
        print("Shoeszise is:",self.shoesize)
        print("City is:",self.city)
#objext creation
obj = person()
#print(obj.name)
#print(obj.name)
obj1 = person()
obj.info()
#print(obj1.name)
obj1.info()
obj.out()
obj1.out()

    