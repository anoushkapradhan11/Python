import math
class Demo:
    def __init__(annu,num):
        annu.num=num
    def square(annu):
        return annu.num**2
    def cube(annu):
        return annu.num**3
    def squareroot(annu):
        return math.sqrt(annu.num)
    @staticmethod
    def greet():
        print("Hello")
c=Demo(4) 
c.greet()   
print(c.square())
print(c.cube())
print(c.squareroot())