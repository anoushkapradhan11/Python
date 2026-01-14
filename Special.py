num=59
m=num
sum=0
prod=1
while m!=0:
    d=m%10
    sum=sum+d
    prod=prod*d
    spec=sum+prod
    m=m//10
if(num==spec):
    print("Yes")
else:
    print("No")