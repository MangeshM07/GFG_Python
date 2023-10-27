def isPalin(N):
    # code here
    n = str(N)
    if len(n) <= 1:
        return 1

    return ((n[0] == n[-1]) and isPalin(n[1:-1]))

n = 101
print(isPalin(n))