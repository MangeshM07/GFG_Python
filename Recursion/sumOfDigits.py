def sumOfDigits(num):
    while num <= 10:
        return num
    return sumOfDigits(num//10)+ (num%10)


print(sumOfDigits(743))

    