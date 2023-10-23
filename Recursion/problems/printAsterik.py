def printAsterik(num):
    if num <= 0:
        return

    printAsterik(num -1)
    print('*' * num)

n = 5
printAsterik(n)