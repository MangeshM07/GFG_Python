def getSmallerElement(mylist, x):
    smaller_element_list = []
    for element in mylist:
        if element < x:
            smaller_element_list.append(element)

    return smaller_element_list


l = [8, 100, 20, 40, 3, 7]
x = 10
print(getSmallerElement(l, x))


l = [100, 20, 40, 60, 80, 90]
x = 60
print(getSmallerElement(l, x))



