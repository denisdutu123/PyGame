class cars():
    def __init__(self, cost, brand):
        self.cost = cost
        self.brand = brand
    def intp(self):
        self.cost = input("How much is your car worth?")
        self.brand = input("What brand is your car")
    def out(self):
        print(self.cost)
        print(self.brand)

obj = cars("Ferrari", 250000)
obj2 = cars("Mercedes", 60000)
obj.out()
obj2.out()
obj.intp()
obj2.intp()
obj.out()
obj2.out()








