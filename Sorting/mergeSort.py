def merge(a, low, mid, high):
    left = a[low:mid+1]
    right = a[mid+1:high+1]
    i=0
    j=0
    k=low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        a[k] = right[j]
        k += 1
        j += 1

    return a


def mergeSort(arr, left, right):
    if right > left:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr

arr = [10, 5, 30, 15, 7]
print(mergeSort(arr, 0, len(arr)-1))
