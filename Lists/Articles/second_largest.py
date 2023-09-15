def second_largest(array):
    if len(array) == 0:
        return "Empty Array"

    largest = float('-inf')
    second_largest  = float('-inf')


    for element in array:
        if element > largest and element > second_largest:
            largest = element
        elif element < largest and element > second_largest:
            second_largest = element

    if second_largest == float('-inf'):
        return largest

    return second_largest


lst = [10, 5, 10]
print(second_largest(lst))

lst = [12, 35, 1, 10, 34, 1]
print(second_largest(lst))

lst = [10, 10, 10]
print(second_largest(lst))