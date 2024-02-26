'''
Introduction:
==============
1) Divide and Conquer Algorithm
2) Worst case time : O(n^2)
3) Despite this it is considered faster because of the following:
    a) In-Place
    b) Cache- friendly
    c) Average case is O(nlog(n))
    d) Tail recursive
4) Partition is key function(naive, Lomuto, Hoars)

'''
def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def qsort(arr, l ,h):
    if l < h:
        p = lomutoPartition(arr, l, h)
        qsort(arr, l , p-1)
        qsort(arr, p+1, h)


arr = [10, 80, 30, 90, 40, 50, 70]
l = 0
h = 6

qsort(arr, l, h)
print(arr)