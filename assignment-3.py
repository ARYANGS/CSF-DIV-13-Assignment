def check(a, b, c):
    if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
        return True
    else:
        return False

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if check(a, b, c):
    print("It is a right angled triangle.")
else:
    print("It is not a right angled triangle.")