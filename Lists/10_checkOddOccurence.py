def getOdd(mylist):
    if len(mylist) < 1:
        return None
    elif len(mylist) == 1:
        return mylist[0]

    for i in range(len(mylist)):
        if mylist.count(mylist[i]) % 2 != 0:
            return mylist[i]


def getOddEasy(l):
    res = 0
    for x in l:
        res = res ^ x
    return res


l = [10, 30, 30, 10, 30, 30, 20]
print(getOdd(l))

l = [10, 10, 10, 10, 10, 20, 20]
print(getOdd(l))

l = [10]
print(getOdd(l))

l = [10, 30, 30, 10, 30, 30, 20]
print(getOddEasy(l))

l = [10, 10, 10, 10, 10, 20, 20]
print(getOddEasy(l))

l = [10]
print(getOddEasy(l))
