with open("file1.txt") as f:
    c=f.readlines()
line=1
for i in c:
    if("Python" in i):
        print(f"Word in line {line}")
        break
    line+=1
else:
    print("Not present")