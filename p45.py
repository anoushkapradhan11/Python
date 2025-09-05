with open("file.txt") as f:
    content=f.read()
if("Donkey"in content):
   c= content.replace("Donkey","####")
print(c)