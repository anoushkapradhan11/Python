import math
class Calculator:
    def __init__(self,num):
        self.num=num
    def square(self):
        return self.num**2
    def cube(self):
        return self.num**3
    def squareroot(self):
        return math.sqrt(self.num)
    @staticmethod
    def greet():
        print("Hello")
c=Calculator(4) 
c.greet()   
print(c.square())
print(c.cube())
print(c.squareroot())