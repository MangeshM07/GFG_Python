def left_rotate_by_1(array):
    if len(array) < 1:
        return "Empty array"
    elif len(array) == 1:
        return array

    first = array[0]
    for i in range(0,len(array)-1):
        array[i] = array[i+1]

    array[len(array)-1] = first

    return array

l = [10, 20, 30, 40]
print(left_rotate_by_1(l))

l = [10, 20, 30, 40]
l = l[1:] + l[0:1]
print(l)

l = [10, 20, 30, 40]
l.append(l.pop(0))

print(l)