def searchInSortedList(n, array):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left + right)//2

        if array[mid] == n:
            return 1
        elif array[mid] < n:
            left = mid + 1
        elif array[mid] > n:
            right = mid - 1

    return -1

arr = [10,20,30,40,50,60,70]
n = 60
print(searchInSortedList(n,arr))