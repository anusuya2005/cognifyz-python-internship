num1=float(input("Enter first number :"))
num2=float(input("Enter second number :"))
operators=["+","-","*","/"]
print(operators)
operator=input("enter the required operator for calcualtion from the above option :")
if operator=="+":
    print("The result is",num1+num2)
elif operator=="-":
    print("The result is",num1-num2)
elif operator=="*":
    print("The result is",num1*num2)
elif operator=="/":
    if num2!=0:
        print("The result is",num1/num2)
    else:
        print("Division by zero not allowed")
else:
    print("Invalid operator")

    


