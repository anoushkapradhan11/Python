def list1(list,index=0):
    if (index==len(list)):
        return
    print(list[index])
    list1(list,index+1)
l1=["a","b","c"]
list1(l1)
