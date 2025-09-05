with open("this.txt") as f:
    content=f.read()
with open("that.txt") as f:
    c=f.read()
if(content==c):
    print("yes")
else:
    print("No")