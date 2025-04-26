a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

if a > b:
    if a > c:
        print("a is max...")
    else:
        print("c is max...")
else:
    if b > c:
        print("b is max...")
    else:
        print("c is max...")