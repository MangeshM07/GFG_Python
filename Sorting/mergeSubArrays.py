def merge(a, low, mid, high):
    left = a[low:mid+1]
    right = a[mid+1:high+1]
    i=0
    j=0
    k=low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            k += 1
            i += 1
        else:
            a[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        a[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        a[k] = right[j]
        k += 1
        j += 1

    return a

a = [10,15,20,40,8,11,55]
low = 0
mid = 3
high = 6

print(merge(a, 0, 3, 6))

