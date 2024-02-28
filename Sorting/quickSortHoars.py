def hoarsPartition(arr, l, h):
    pivot = arr[l]
    i = l - 1
    j = h + 1
    while True:
        i = i+1
        while arr[i] < pivot:
            i = i+1

        j = j-1
        while arr[j] > pivot:
            j = j-1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]



def qsort(arr, l ,h):
    if l < h:
        p = hoarsPartition(arr, l, h)
        qsort(arr, l , p)
        qsort(arr, p+1, h)


arr = [10, 80, 30, 90, 40, 50, 70]
l = 0
h = 6

qsort(arr, l, h)
print(arr)