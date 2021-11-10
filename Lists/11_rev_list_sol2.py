def rev(mylist):
    if len(mylist) <= 1:
        return mylist
    else:
        start = 0
        end = len(mylist) - 1
        while start < end:
            mylist[start], mylist[end] = mylist[end], mylist[start]
            start += 1
            end -= 1
        return mylist


if __name__ == '__main__':
    l = [10, 20, 3, 4, 10, 20, 7, 3]
    print(rev(l))

    l = [10]
    print(rev(l))

    l = [10, 30, 30, 10, 30, 30, 20]
    print(rev(l))

    l = [10, 20, 30, 40, 50]
    print(rev(l))

    nl = []
    nl[:0] = "MANGESH"
    print(rev(nl))
