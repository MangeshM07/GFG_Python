def printNumber1toN(number):
    if number <= 0:
        return
    printNumber1toN(number - 1)
    print(number, end=' ')

number = 5
printNumber1toN(number)