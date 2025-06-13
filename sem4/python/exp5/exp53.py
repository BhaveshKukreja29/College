#Overload the > operator

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, object):
        if not isinstance(object, Person):
            return "Object type mismatch"
        else:
            return self.age > object.age


p1 = Person("Bhavesh", 20)
p2 = Person("Darsh", 34208)

print(p1 > p2)
print(p2 > p1)
