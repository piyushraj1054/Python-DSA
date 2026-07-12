num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter operator (+, -, *, /): ")

if operator=='+':
    result=num1+num2
    print("The result of addition is:", result)
elif operator=='-':
    result=num1-num2
    print("The result of subtraction is:", result)
elif operator=='*':
    result=num1*num2
    print("The result of multiplication is:", result)
elif operator=='/':
    result=num1/num2
    print("The result of division is:", result)
else:
    print("Invalid operator")