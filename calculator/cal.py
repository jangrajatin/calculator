print("Welcome to this calculator")
print("you'll see some opertor")

num1 = int(input("Enter your 1st value:\n"))
num2 = int(input("Enter your 2nd value:\n"))
operator = input("+ , -, X , /\n:")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "X" or "x":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("this is not valid oprator")