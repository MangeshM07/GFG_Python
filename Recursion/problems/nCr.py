# You are given two numbers n and r. You need to find nCr.
# nCr = (n!) / ((n-r)!*(r!))
# In recursive way, we can write nCr as nCr = (n-1)C(r-1) + (n-1)Cr

def factorial(n):
    if n <= 1:
        return 1

    return factorial(n - 1) * n


def nCr(n, r):
    # code here
    return factorial(n) // (factorial(n - r) * factorial(r))

n = 5
r = 2
print(nCr(n,r))