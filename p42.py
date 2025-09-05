f=open("Poems.txt")
c=f.read()
if("Twinkle"in c):
    print("Yes")
else:
    print("No")
f.close()
