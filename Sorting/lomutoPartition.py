def lomutoPartition(arr, l , pivotIndex):
    pivot = arr[pivotIndex]
    i = l-1

    for j in range(l,pivotIndex):
        if arr[j] < pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[pivotIndex] = arr[pivotIndex], arr[i+1]
    return arr

arr  = [10,80,30,90,50,70]
l=0
h=5
print(lomutoPartition(arr,l,h))