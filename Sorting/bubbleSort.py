def bubbleSort(l):
    numOfElements = len(l)

    swapped = False
    for i in range(numOfElements-1):
        for j in range(numOfElements-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1], l[j]
                swapped = True

            if swapped == False:
                print("Not Swapped")
                return l

    return l

arr = [10,3,7,15, 2]
arr1 = [5,10,15,20]

print(bubbleSort(arr))