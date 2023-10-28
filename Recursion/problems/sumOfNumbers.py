def sumOfNumbers(n):
    if n <= 1:
        return 1

    return sumOfNumbers(n-1) + n

n = 4
print(sumOfNumbers(n))