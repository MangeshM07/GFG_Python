def partitionArray(array, position):
    arr1 = []
    arr2 = []

    for item in array:
        if item <= array[position]:
            arr1.append(item)
        else:
            arr2.append(item)

    return arr1+arr2

l = [3,8,6,12,10,7]
p = 5

print(partitionArray(l,p))
