def searchInSorted(arr, N, k):
    low = 0
    high = N - 1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == k:
            return True
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1
    return False

arr = [1,2,3,4, 6]
print(searchInSorted(arr, 5, 2))