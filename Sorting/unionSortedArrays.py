def unionSortedArrays(array1, array2):
    i=0
    j=0
    array =[]

    while (i < len(array1) and j < len(array2)):
        if (i > 0 and array1[i] == array1[i-1]):
            i += 1
        elif (j > 0 and array2[j] == array2[j-1]):
            j += 1
        elif array1[i] < array2[j]:
            array.append(array1[i])
            i += 1
        elif array1[i] > array2[j]:
            array.append(array2[j])
            j += 1
        else:
            i += 1
            j += 1

    while (i<len(array1)):
        if (i>0 and array1[i] != array1[i-1]):
            array.append(array1[i])
            i += 1

    while (j < len(array2)):
        if (j>0 and array2[j] != array2[j-1]):
            array.append(array2[j])
            j += 1

    return array


array1 = [3, 5, 8, 8]
array2 = [2,8,9,10,15]

print(unionSortedArrays(array1, array2))
