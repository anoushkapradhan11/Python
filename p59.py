class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
class ThreeDVector(TwoDVector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
T=TwoDVector(2,3)
print(f"{T.i}i+{T.j}j")
t=ThreeDVector(4,5,6)
print(f"{t.i}i+{t.j}j+{t.k}k")

