# def avgList(mylist):
#     return sum(mylist) / len(mylist)
#
#
def avgList(lst):
    sum=0
    count=0
    for item in lst:
        sum += item
        count +=1

    return sum/count


lst = [10, 20, 30, 40]
print(avgList(lst))
