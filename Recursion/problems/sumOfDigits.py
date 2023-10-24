def sumofDigits(num):
    if num < 10:
        return num

    return sumofDigits(num//10) + (num%10)

num = 9999
print(sumofDigits(num))