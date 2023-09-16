def isSorted(array):
    sorted_array = sorted(array)

    if array == sorted_array:
        return True
    else:
        return False

l = [10,20,30,15,40]
print(isSorted(l))