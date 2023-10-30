def f(x,y):
    if x == 0 :
        return y
    else:
        return f(x-1, x+y)

# print(f(4,3))

def fun(n):
    if n <= 1:
        return 1

    if n % 2==0:
        return fun(n//2)

    return fun(n//2) + fun(n//2+1)

print(fun(11))