def bSearch_first_occurrence(input_list, search_value):
    low = 0
    high = len(input_list)-1

    while (low <= high):
        mid = (low+high)//2

        if input_list[mid] < search_value:
            low = mid+1
        elif input_list[mid] > search_value:
            high = mid-1
        else:
            if mid==0 or input_list[mid-1] != input_list[mid]:
                return mid
            else:
                high = mid-1
    return -1

l = [1,1, 10,10,10,20,20,40]

print(20, bSearch_first_occurrence(l, 20))
print(10, bSearch_first_occurrence(l, 10))
print(1, bSearch_first_occurrence(l, 1))

b = [5,10,10,20,20]

print(5, bSearch_first_occurrence(b, 5))
print(10, bSearch_first_occurrence(b, 10))
print(20, bSearch_first_occurrence(b, 20))