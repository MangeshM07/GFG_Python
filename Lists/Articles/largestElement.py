def get_largest_element(array):
    return max(array)

def get_largest_element_n(array):
    if len(array) == 0:
        return "Empty array"
    largest = float('-inf')

    for element in array:
        if element > largest:
            largest = element
    return largest

list1 = [10, 20, 4]
list2 = [-10, -50, -50, -100]

print(get_largest_element_n(list2))