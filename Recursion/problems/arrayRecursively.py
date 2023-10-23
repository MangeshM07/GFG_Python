def arrayRecursively(arr, index , n):
    if index >= n:
        return

    print(arr[index], end=' ')
    arrayRecursively(arr, index + 1, n)


n = 4
arr = [5,4,2,1]
arrayRecursively(arr, 0, n)