def selection_sort(array):
    numberOfElements = len(array)

    for i in range(numberOfElements-1):
        minimumIndex = i
        for j in range(i+1, numberOfElements-1):
            if array[j] < array[minimumIndex]:
                minimumIndex = j
        array[i], array[minimumIndex] = array[minimumIndex], array[i]

    return array


arr = [10,3,7,15]
arr1 = [5,10,15,20]

print(selection_sort(arr1))