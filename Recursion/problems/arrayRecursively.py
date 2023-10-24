def arrayRecursively(arr, index , n):
    if index >= n:
        return

    print(arr[index], end=' ')
    arrayRecursively(arr, index + 1, n)

def arrayRecursively_sol2(arr, n):
    if n <= 0:
        return

    arrayRecursively_sol2(arr, n-1)
    print(arr[n-1], end=' ')

n = 4
arr = [5,4,2,1]
arrayRecursively_sol2(arr, n)