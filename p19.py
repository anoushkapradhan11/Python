marks=int(input("Enter the marks:"))
if(marks in range(90,101)):
    print("Ex")
elif(marks in range(80,91)):
    print("A")
elif(marks in range(70,81)):
    print("B")
elif(marks in range(60,71)):
    print("C")
elif(marks in range(50,61)):
    print("D")
elif(marks < 50):
    print("F")