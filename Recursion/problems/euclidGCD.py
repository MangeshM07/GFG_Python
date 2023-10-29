def GCD(a,b):
    if b == 0:
        return a
    return GCD(b, a%b)

a= 48
b = 18
result = GCD(a, b)
print(result)