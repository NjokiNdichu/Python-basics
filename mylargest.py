num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
num3=float(input("Enter third number: "))


if (num1>num2) and (num1>num3):
    print(num1)
elif (num2>num1) and (num2>num3):
    print(num2)
elif (num3>num1) and (num3>num2):
    print(num3)
else:
    print("They are equal")