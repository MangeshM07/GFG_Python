def largestElement(lst):
    return max(lst)


def largestElement_custom(lst):
    if len(lst) == 0:
        return None

    max = lst[0]
    for i in lst:
        if (i > max):
            max = i
    return max


inputList = [10, 5, 20, 8]
print(largestElement_custom(inputList))


inputList = [-3, -2, -1]
print(largestElement_custom(inputList))
