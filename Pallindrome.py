num=121
temp=num
sum=0
while temp!=0:
    d=temp%10
    sum=sum*10+d
    temp=temp//10
if(num==sum):
    print("Yes")
else:
    print("No")
