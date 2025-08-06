
print("Hello World!")


def Sum(a,b,operation="add"):
    if operation == "subs":
        return a-b
    return a+b

print("Sum : ",Sum(4,5))
print("Sum : ",Sum(4,5,"subs"))