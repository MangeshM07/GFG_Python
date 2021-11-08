def isSorted(mylist):
    sorted_list = sorted(mylist)

    if mylist == sorted_list:
        return True
    else:
        return False

    
l = [10, 20, 30, 40]
if isSorted(l):
    print("Yes, List is sorted")
else:
    print("No, List is not sorted")

