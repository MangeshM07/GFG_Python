def checkSubset(list1, list2):
    l1, l2 = list1[0], list2[0]
    exist = True
    for i in list2:
        if i not in list1:
            exist = False
    return exist


# Driver Code
list1 = [[2, 3, 1], [4, 5], [6, 8]]
list2 = [[4, 5], [6, 8]]
print(checkSubset(list1, list2))


def checkSubset(list1, list2):
    temp1 = []
    temp2 = []
    for i in list1:
        temp1.append(tuple(i))
    for i in list2:
        temp2.append(tuple(i))
    print(temp1)
    print(temp2)
    return set(temp2) < set(temp1)


# Driver Code
list2 = [[2, 3, 1], [4, 5], [6, 8]]
list1 = [[4, 5], [6, 8]]
print(checkSubset(list1, list2))