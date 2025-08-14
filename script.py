print('''
This app is a calculator
It will perform some operations
''')

def calcultaor(a,b,operation="add"):
    if operation == "sub":
        return a-b
    elif operation == "mul":
        return a*b
    elif operation == "div":
        return a/b
    elif operation == "mod":
        return a%b
    else:
        return a+b

a,b = 4,5
print("  Calculator  ".center(50,"="))
print(f"a = {a} , b = {b}")
print(f"Sum  {a} + {b} : ",calcultaor(a,b,"add"))
print(f"Mul  {a} * {b} : ",calcultaor(a,b,"mul"))
print(f"Div  {a} / {b} : ",calcultaor(a,b,"div"))
print(f"Sub  {a} - {b} : ",calcultaor(a,b,"sub"))
print(f"Mod  {a} % {b} : ",calcultaor(a,b,"mod"))