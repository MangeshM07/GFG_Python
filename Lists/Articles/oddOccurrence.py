def odd_occurence(array):
    res=0

    for element in array:
        res = res ^ element

    return res


# Test array
arr = [ 2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]

print("%d" % odd_occurence(arr))