def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    print(n)



def fun2(n):
    if n==0:
        return
    fun2(n-1)
    print(n)
    fun2(n-1)


def fun3(n):
    if n <= 1:
        return 0
    else:
        return 1 + fun3(n//2)


def fun4(n):
    if n==0:
        return
    fun4(n//2)
    print(n%2)


# print(fun3(16))
fun4(13)
