def searchElement(arr, N, X):
    for i in range(len(arr)):
        if arr[i] == X:
            return i

    return -1
