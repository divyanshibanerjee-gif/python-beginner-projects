operation = str(input("Enter operation (+, -, *, /, %, sqrt, **): "))

num1 = float(input("Enter first number: "))

if operation == "sqrt":
    if num1<0:
        print("Cannot calculate square root of a negative number")
    else:
        print("Result =", num1 ** 0.5)

else:
    num2 = float(input("Enter second number: "))

    if operation == "+":
        print("Result =", num1 + num2)

    elif operation == "-":
        print("Result =", num1 - num2)

    elif operation == "*":
        print("Result =", num1 * num2)

    elif operation == "/":
        if num2==0:
            print("Cannot divide a number by 0")
        else:
            print("Result=", num1/num2)
    
    elif operation == "%":
        if num2 == 0:
            print("Cannot calculate remainder when divided by zero")
        else:
            print("Result =", num1 % num2)
    elif operation == "**":
        print("Result=", num1**num2)

    else:
        print("Invalid operation")
