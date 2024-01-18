def bubble_sort(array):
    swapped = False
    numberOfElements = len(array)

    for i in range(numberOfElements-1):
        for j in range(numberOfElements - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

            if swapped == False:
                print("not swapped")
    return array

arr = [10,3,7,15, 2]
arr1 = [5,10,15,20]

print(bubble_sort(arr))
