def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid+1
    k = left
    inv_count = 0

    while i <= mid and j<= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
            inv_count += (mid-i+1)
        k+=1

    while i <= mid:
         temp_arr[k] = arr[i]
         i += 1
         k += 1


    while j<= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for p in range(left, right+1):
        arr[p]=temp_arr[p]

    return inv_count

def mergeSort(arr, temp_arr, left, right):
    inv_count = 0

    if left < right:
        mid = (left+right)//2

        inv_count += mergeSort(arr, temp_arr, left, mid)
        inv_count += mergeSort(arr,temp_arr, mid+1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count


def countInversions(arr):
    n = len(arr)
    temp_arr = [0]*n
    return mergeSort(arr, temp_arr, 0, n-1)


arr = [1, 20, 6, 4, 5]
print("Number of inversions:", countInversions(arr))