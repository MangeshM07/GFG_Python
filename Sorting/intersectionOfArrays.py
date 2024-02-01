# def intersectionOfArrays(array1, array2):
#     array1 = list(set(array1))
#     array2 = list(set(array2))
#
#     for i in array1:
#         if i in array2:
#             print(i)

# O(m+n) time | O(1) space
# This solution will work only for sorted arrays
def intersectionOfArrays(array1, array2):
    i=j=0

    while i < len(array1) and j < len(array2):
        if i>0 and array1[i] == array1[i - 1]:
            i += 1
            continue

        if array1[i] < array2[j]:
            i += 1
        elif array1[i] > array2[j]:
            j += 1
        else:
            array1[i] == array2[j]
            print(array1[i])
            i += 1
            j += 1


a = [3,5,10,10,10,15,15,20]
b = [5,10,10,15,30]

intersectionOfArrays(a,b)