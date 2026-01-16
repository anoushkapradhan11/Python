arr=[2,3,4,5,9,8]
second=largest=-1
for i in arr:
    if i>largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)