def selectionSort(l):
    n = len(l)

    for i in range(n-1):
        min_ind = i
        for j in range(i+1, n):
            if l[j] < l[min_ind]:
                min_ind = j
        l[min_ind], l[i] =  l[i] , l[min_ind]

    return l

arr = [10,3,7,15]
arr1 = [5,10,15,20]

print(selectionSort(arr))
