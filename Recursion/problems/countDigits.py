def countDigits(n):
    if n < 10:
        return 1

    return countDigits(n//10) + 1

num = 999
print(countDigits(num))