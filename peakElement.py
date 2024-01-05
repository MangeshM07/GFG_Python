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

array = [3,4,2]
array1=[1,2,3]
print(peakElement(array1,3))