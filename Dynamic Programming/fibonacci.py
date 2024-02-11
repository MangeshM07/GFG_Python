memo = [None]*100
def fibonacci(n):
    if memo[n] != None:
        return memo[n]
    if n==0 or n==1:
        memo[n] = n
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

print(fibonacci(5))