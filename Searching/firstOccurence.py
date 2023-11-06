def indexOfFirstOccurence(arr, element):
    low = 0
    high = len(arr)-1
    result = -1

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == element:
            result = mid
            high = mid - 1
        elif arr[mid] < element:
            low = mid + 1
        elif arr[mid] > element:
            high = mid -1


    return result

arr = [1, 10, 10, 10, 20, 20, 40]
print(indexOfFirstOccurence(arr, 10))