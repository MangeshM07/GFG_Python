def peakElement(array,n):
    # check the first element
    if n==1 or array[0]>array[1]:
        return 0

    # check the last element
    if array[n-1] > array[n-2]:
        return n-1

    # check the elements in the middle
    for i in range(1, n-1):
        if array[i-1] < array[i]  > array[i+1]:
            return i


def peakElementUsingBinarySearch(array,n):
    if n == 0:
        return None
    elif n==1:
        return 0
    elif n==2:
        if array[0] > array[1]:
            return 0
        else:
            return 1

    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        if array[mid-1] <= array[mid] and array[mid] >= array[mid+1]:
            return mid
        elif mid != 0 and array[mid] < array[mid-1]:
            high = mid -1
        elif array[mid] < array[mid+1] and mid+1 == n-1 :
            return mid+1
        else:
            low = mid + 1

    return -1

array = [3,4,2]
array1=[1,2,3,4]
array2 = [497, 850, 64, 479, 511, 958]
print(peakElementUsingBinarySearch(array2,6))