arr=[3,4,5,6,0,2]
max=arr[0]
min=arr[0]
for i in arr:
    if i>max:
        max=i
    if i<min:
        min=i
print(max)
print(min)