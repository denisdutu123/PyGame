class keyboard():
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    def intp(self):
        self.brand = input("What brand is your keyboard?")
        self.size = input("What is the size of the keyboard?")
    def out(self):
        print(self.brand)
        print(self.size)

obj = keyboard("Logitic", 10)
obj2 = keyboard("Razor", 8)
obj.out()
obj2.out()
obj.intp()
obj2.intp()
obj.out()
obj2.out()

