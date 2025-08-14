def remove(list1,l):
    n=[]
    for i in list1:
        if not(i==l):
            n.append(i.strip(l))
        return n
     
list1=["Mohit","Mohan","an"]
print(remove(list1,"an"))

