def natural_numbers(num):
    if(num==1):
        return 1
    return natural_numbers(num-1)+num
n=int(input("Enter the number:"))
print("Sum of n natural numbers are:",natural_numbers(n))