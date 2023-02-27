a = float(input("a: "))
eps = float(input("eps: "))
x = a
x0 = 0.0
while (abs(x - x0) > eps):
    x0 = x
    x = (x0 + a / x0) / 2

print(x)
