def fun_N_till_1(n):
    if n==0:
        return
    fun_N_till_1(n-1)
    print(n)

def fun_1_till_N(n):
    if n==0:
        return
    print(n)
    fun_1_till_N(n-1)

def fun_sum_of_digits(n):
    if n< 10:
        return n
    return fun_sum_of_digits(n//10) + (n%10)


print(fun_sum_of_digits(984))