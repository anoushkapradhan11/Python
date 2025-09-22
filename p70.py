try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError as z:
    print("Infinite")
else:
    print("Sucess!!")