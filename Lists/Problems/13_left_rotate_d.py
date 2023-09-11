# Using list slicing
def left_rotate_d_method1(mylist, d):
    newlist = mylist[d:] + mylist[0:d]
    return newlist


# Using deque
from collections import deque


def left_rotate_d_method2(mylist, d):
    dq = deque(mylist)
    dq.rotate(-d)
    l = list(dq)
    print(l)


# Using own methods
def left_rotate_d_method3(mylist, d):
    newlist = []
    n = len(mylist)

    for i in range(0, n - d):
        newlist.append(mylist[i + d])

    for i in range(0, d):
        newlist.append(mylist[i])

    return newlist


#  Using own method - GFG
def left_rotate_d_method4(mylist, d):
    for i in range(0, d):
        mylist.append(mylist.pop(0))
    return mylist


# Bettter solution - GFG
def left_rotate_d_method5(mylist,d):
    n = len(mylist)
    reverse_list(mylist, 0, d-1)
    reverse_list(mylist, d, n-1)
    reverse_list(mylist, 0, n-1)
    return mylist

def reverse_list(mylist, b, e):
    while b < e:
        mylist[b], mylist[e] = mylist[e], mylist[b]
        b = b+1
        e = e-1
    return mylist


l = [10, 20, 3, 4, 10, 20, 7, 3]
print(l)
print(reverse_list(l,0,7))

print(left_rotate_d_method5(l, 3))
#
# l = [10]
# print(left_rotate_d_method1(l))
#
# l = [10, 20, 3, 4, 10, 20, 7, 3]
# print(left_rotate_d_method1(l))
#
# l = [10]
# print(left_rotate_d_method1(l))
#
# l = [10, 20, 3, 4, 10, 20, 7, 3]
# print(left_rotate_d_method1(l))
#
# l = [10]
# print(left_rotate_d_method1(l))
#
# l = [10, 20, 3, 4, 10, 20, 7, 3]
# print(left_rotate_d_method1(l))
#
# l = [10]
# print(left_rotate_d_method1(l))
