def floorInSortedArray(arr, N, x):
    if x < arr[0]:
        # If x is smaller than the smallest element in arr
        return -1

    low, high = 0, N - 1
    floor_index = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            # If arr[mid] is equal to x, it is the largest element <= x
            return mid
        elif arr[mid] < x:
            # Update floor_index and search in the right half
            floor_index = mid
            low = mid + 1
        else:
            # Search in the left half
            high = mid - 1

    return floor_index

N = 7
x = 0
arr = [1,2,8,10,11,12,19]
print(floorInSortedArray(arr, N, x))


N1 = 7
x1 = 5
arr1 = [1,2,8,10,11,12,19]
print(floorInSortedArray(arr1, N1, x1))