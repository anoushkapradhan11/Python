marks1=int(input("Enter the marks:"))
marks2=int(input("Enter the marks:"))
marks3=int(input("Enter the marks:"))
total=(100*(marks1+marks2+marks3))/300
if(total>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Passed")
else:
    print("Failed")

