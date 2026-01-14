num=123
m=num
sum=0
prod=1
while m!=0:
    d=m%10
    sum=sum+d
    prod=prod*d
    m=m//10
if sum==prod:
    print("Yes")
else:
    print("No")