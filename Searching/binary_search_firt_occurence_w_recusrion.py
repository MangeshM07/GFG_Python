def searchInSortedListRecursively(array, n, low, high):
    if low > high :
        return -1

    mid = (low + high)//2
    if array[mid] == n:
        return 1
    elif array[mid] > n:
        return searchInSortedListRecursively(array, n, low, mid - 1)
    elif array[mid] < n:
        return searchInSortedListRecursively(array, n, mid + 1, high)

    return -1


def bSearchMain(arr, n):
    return searchInSortedListRecursively(arr, n, 0, len(arr) - 1)



arr = [10, 20, 30, 40, 50, 60, 70]
n = 60
print(bSearchMain(arr, n))
