num=153
m=num
sum=0
while m!=0:
    d=m%10
    sum=sum+d**3
    m=m//10
if(sum==num):
    print("Yes")
else:
    print("No")