def insertionSort(array):
    for i in range(1, len(array)):
        x = array[i]
        j = i - 1
        while j >= 0 and x < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = x
    return array


array = [20, 5, 30, 40, 10, 60]
print(insertionSort(array))
