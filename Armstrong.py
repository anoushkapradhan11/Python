num=153
m=num
sum=0
dig=len(str(num))
while m!=0:
    d=m%10
    sum=sum+d**dig
    m=m//10
if(sum==num):
    print("Yes")
else:
    print("No")