def sequence(num):
    if num == 0:
        return 1
    return num + (num * sequence(num - 1))

num = 3
print(sequence(num))
