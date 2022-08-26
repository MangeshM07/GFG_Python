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

###############################################################
def check_list_sorted(l):
    if len(l) == 1 or len(l) == 0:
        return True
    else:
        for i in range(0, len(l)-1):
            if l[i] <= l[i+1]:
                continue
            else:
                return False
        return True


l = [10, 20, 20, 30]
print(check_list_sorted(l))

l = [10, 5, 2]
print(check_list_sorted(l))

l = [10]
print(check_list_sorted(l))

l = []
print(check_list_sorted(l))

l = [10, 5, 30]
print(check_list_sorted(l))