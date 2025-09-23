from functools import reduce
l=[4,5,6,7,8,9,10,20]
def greater(a,b):
    if(a>b):
        return a
    else:
        return b
print(reduce(greater,l))