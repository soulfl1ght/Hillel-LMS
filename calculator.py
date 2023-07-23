a = int(input("Type a:"))
b = int(input("Type b:"))
operation_type = input("Type operation type:")
if operation_type == "addition":
    print(a+b)
elif operation_type == "subtraction":
    print(a-b)
elif operation_type == "multiplication":
    print(a*b)
elif operation_type == "division" and b == 0 and a>0 or a<0:
    print("Oops! Mistake! You can't divide by zero!")
elif operation_type == "division":
    print(a/b)