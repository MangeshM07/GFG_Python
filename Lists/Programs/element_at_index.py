def getByIndex(arr,n, idx):
    if idx >= n:
        return -1
    else:
        return arr[idx]


n = 6
arr = [1, 2 ,3, 4 ,5, 6]
index = 0

print(getByIndex(arr, n, index))

n = 4
arr = [1, 2, 3, 4]
index = 4

print(getByIndex(arr, n, index))