# Given a sorted array, the task is to remove the duplicate elements from the array.

def remove_duplicates(array):
    unique_list = []

    for i in array:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list, len(unique_list)

def inplace_remove_duplicates(array):

    i=0
    while i < len(array)-1:
        if array[i] == array[i+1]:
            array.pop(i+1)
        else:
            i += 1

    return array

arr = [2, 2, 2, 2, 2]
# print(remove_duplicates(arr))

print(inplace_remove_duplicates(arr))

