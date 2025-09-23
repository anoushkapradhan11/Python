list1=[2,4,5,10,90,89,76,75]
def num(n):
    if(n%5==0):
        return True
    return False
print(list(filter(num,list1)))