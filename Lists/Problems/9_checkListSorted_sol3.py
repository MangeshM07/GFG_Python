def checkListSorted(input_list):
    if len(input_list) <= 1:
        return "Length of the list should be greater than 1"

    for i in range(0, len(input_list)-1):
        if input_list[i] <= input_list[i+1]:
            continue
        else:
            return False

    return True

def checkListSorted_sorted(input_list):
    sorted_list  = sorted(input_list)

    if input_list == sorted_list:
        return True
    else:
        return False


l = [10, 20, 20, 30]
print(checkListSorted_sorted(l))

