def get_smaller_elements(array, num):
    smaller_list = []
    for i in array:
        if i < x:
            smaller_list.append(i)

    return smaller_list

arr = [8, 100, 20, 40, 3, 7]
x = 10

print(get_smaller_elements(arr,x))
