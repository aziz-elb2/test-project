
print("Hello World!")


def Sum(a,b,operation="add"):
    if operation == "sub":
        return a-b
    elif operation == "mul":
        return a*b
    elif operation == "div":
        return a/b
    else:
        return a+b

a,b = 4,5
print("Test other operations ......")
print(f"a = {a} , b = {b}")
print("Sum : ",Sum(a,b,"add"))
print("Mul : ",Sum(a,b,"mul"))
print("Div : ",Sum(a,b,"div"))
print("Sub : ",Sum(a,b,"sub"))