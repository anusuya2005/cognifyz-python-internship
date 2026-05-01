temp=int(input("Enter Temperature: "))
unit=input("Enter unit: ").upper()
if unit=="C":
    print("The converted Fahrenheit temperature is",((temp*9/5)+32))
elif unit=="F":
    print("The converted Celsius temperature is",((temp-32)*5/9))
else:
    print("invalid input")

              
