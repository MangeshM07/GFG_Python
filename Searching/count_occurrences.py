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

def bSearch_last_occurrence(input_list, search_value):
    low = 0
    high = len(input_list)-1

    while (low <= high):
        mid = (low+high)//2

        if input_list[mid] < search_value:
            low = mid+1
        elif input_list[mid] > search_value:
            high = mid-1
        else:
            if mid==len(input_list)-1 or input_list[mid] != input_list[mid+1]:
                return mid
            else:
                low = mid+1
    return -1

def bSearch_count(input_list, search_item):
    first = bSearch_first_occurrence(input_list, search_item)

    if first == -1:
        return 0
    else:
        return bSearch_last_occurrence(input_list, search_item) - first + 1


b = [5,10,10,20,20,20]

# print(bSearch_first_occurrence(b,10))
# print(5, bSearch_count(b, 5))
# print(10, bSearch_count(b, 10))
print(20, bSearch_count(b, 20))