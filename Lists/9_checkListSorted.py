def checkList(mylist):
    if len(mylist) <= 1:
        return True

    for i in range(len(mylist)-2):
        if mylist[i] <= mylist[i+1]:
            continue
        else:
            return False
    return True


l = [10, 20, 30]
print(checkList(l))

l = [10, 20, 20, 30]
print(checkList(l))

l = [10, 5, 2]
print(checkList(l))

l = [10]
print(checkList(l))

l = []
print(checkList(l))

l = [10, 5, 30]
print(checkList(l))

