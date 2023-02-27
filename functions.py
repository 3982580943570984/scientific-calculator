def heron_method(a: float, eps: float):
    x = a
    x0 = 0.0
    while (abs(x - x0) > eps):
        x0 = x
        x = (x0 + a / x0) / 2
    return x


a = float(input("a: "))
eps = float(input("eps: "))

print(heron_method(a, eps))
