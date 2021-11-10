def leftrotate_method1(mylist):
    newlist = mylist[1:] + mylist[0:1]
    return newlist


def leftrotate_method2(mylist):
    mylist.append(mylist.pop(0))
    return mylist


def leftrotate_method3(mylist):
    newlist = []
    newlist = mylist[1:]
    newlist.append(mylist[0])
    return newlist


def leftrotate_method4(mylist):
    n = len(mylist)
    x = mylist[0]
    for i in range(1, n):
        mylist[i - 1] = mylist[i]
    mylist[n - 1] = x
    return mylist


if __name__ == '__main__':
    l = [10, 20, 3, 4, 10, 20, 7, 3]
    print(leftrotate_method1(l))

    l = [10]
    print(leftrotate_method1(l))

    l = [10, 20, 3, 4, 10, 20, 7, 3]
    print(leftrotate_method2(l))

    l = [10]
    print(leftrotate_method2(l))

    l = [10, 20, 3, 4, 10, 20, 7, 3]
    print(leftrotate_method3(l))

    l = [10]
    print(leftrotate_method3(l))

    l = [10, 20, 3, 4, 10, 20, 7, 3]
    print(leftrotate_method4(l))

    l = [10]
    print(leftrotate_method4(l))
