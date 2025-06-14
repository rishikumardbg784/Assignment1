num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
Add=num1+num2
Sub=num1-num2
mult=num1*num2
print("Addition: ",Add)
print("Substraction: ",Sub)
print("Multiplication",mult)

if(num2!=0):
    Div=num1/num2
    print("Divison: ", Div)
else:
    print("Error! Division by zero is not allowed")
