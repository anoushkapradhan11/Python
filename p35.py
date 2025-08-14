def celcius_to_fahrenheit(temperature):
    f=((9/5)*temperature)+32
    return f
temp=float(input("Enter the temperature:"))
print("The temperature in fahrenheit is:",round(celcius_to_fahrenheit(temp)))