words=["Donkey","Kutta","Shit","Dumb"]
with open("file.txt") as f:
    content=f.read()
for i in words:
    content=content.replace(i,"#"*len(i))
print(content)

