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

def avgListUsingsum(lst):
    return sum(lst)/len(lst)


lst = [10, 20, 30, 40, 50]
print(avgList(lst))


lst = [10, 20, 30, 40, 50]
print(avgListUsingsum(lst))

