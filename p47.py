with open("file1.txt") as f:
    c=f.read()
if("Python"or "python" in c):
    print("yes it contains")
else:
    print("Doesn't contain")