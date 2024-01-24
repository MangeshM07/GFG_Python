def mergeLists(array1, array2):
    res = []
    m = len(array1)
    n = len(array2)
    i=0
    j=0

    while i<m and j<n:
        if array1[i] < array2[j]:
            res.append(array1[i])
            i += 1
        else:
            res.append(array2[j])
            j += 1

    while i < m:
        res.append(array1[i])
        i += 1

    while j < n:
        res.append(array2[j])
        j += 1

    return res

a = [10,15]
b = [5,6,6,30,45]
print(mergeLists(a,b))