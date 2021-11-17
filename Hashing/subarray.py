# Subarray with 0 sum with python

# Simple solution
def isZero(l):
    n = len(mylist)
    for i in range(0, n):
        for j in range(i + 1, n + 1):
            if sum(mylist[i:j]) == 0:
                return True
    return False


# Efficient solution
def isZeroSum(l):
    pre_sum = 0
    h = set(l)
    for i in range(len(l)):
        pre_sum += l[i]
        if pre_sum == 0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False


mylist = [1, 4, 13, -3, -10, 5]
print(isZero(mylist))

mylist = [3, 4, -3 -1, 1]
print(isZeroSum(mylist))


