num=int(input("Enter the number:"))
prod=[num*i for i in range(1,11)]
with open("Tables.txt","a") as t:
    t.write(str(prod)+"\n")