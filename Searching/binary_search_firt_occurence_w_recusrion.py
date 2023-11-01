def searchInSortedListRecursively(n, array, left, right):
    if left <= right:
        mid = (left + right)//2

        if array[mid] == n:
            return 1
        elif array[mid] < n:
            searchInSortedListRecursively(n, array, left, mid-1)
        elif array[mid] > n:
            searchInSortedListRecursively(n, array, mid+1, right)

    return -1

arr = [10,20,30,40,50,60,70]
n = 60
left = 0
right = len(arr)-1
print(searchInSortedListRecursively(n,arr, left , right))