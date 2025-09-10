class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    def __add__(self,c):
        return Complex(self.r+c.r,self.i+c.i)
    def __str__(self):
        return f"{self.r}r+{self.i}i"
    def __mul__(self,c):
        real=self.r*c.r-self.i*c.i
        img=self.i*c.i+self.i*c.i
        return Complex(real,img)
    def __str__(self):
        return f"{self.r}r+{self.i}i"
c1=Complex(2,3)
c2=Complex(4,5)
print(c1+c2)
print(c1*c2)