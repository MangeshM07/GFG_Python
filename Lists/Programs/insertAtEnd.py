# You only need to insert the given element at
# the end, i.e., at index sizeOfArray - 1. You may
# assume that the array already has sizeOfArray - 1
# elements.
def insertAtEnd(arr, sizeOfArray, element):
    arr.insert(sizeOfArray - 1, element)
    return arr



arr = [10,5,19,8,5]
size = 5
element = 22

print(insertAtEnd(arr,size,element))