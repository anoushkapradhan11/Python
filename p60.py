class Animals:
    print("This is the animal class")
class Pets(Animals):
    print("This is the pet class")
class Dog(Pets):
    @staticmethod
    def bark():
        print("Woof!!")
d=Dog()
d.bark()