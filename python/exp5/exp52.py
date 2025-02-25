#Python program to demo Multiple inheritance

class Rice:
    def __init__(self, rice):
        self.rice = rice

class Curry:
    def __init__(self, curry):
        self.curry = curry

class Dish(Rice, Curry):
    def __init__(self, rice, curry, cutl):
        self.cutl = cutl
        Rice.__init__(self, rice)
        Curry.__init__(self, curry)

    def __str__(self):
        return f"Nice Dish, enjoy {self.rice} with {self.curry} with your {self.cutl}"

dish1 = Dish("rice", "dal", "hands")
print(dish1)

dish2 = Dish("rice", "milk", "spoon")
print(dish2)
