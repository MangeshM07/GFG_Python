def naive_search_subarray_sum(mylist, subarr_sum):
    if len(mylist) <= 1:
        if sum(mylist[:]) == subarr_sum:
            return True
    else:
        for i in range(len(mylist)):
            curr = 0
            for j in range(i, len(mylist)):
                curr += mylist[j]
                if curr == subarr_sum:
                    return True
    return False


def efficient_search_subarray_sum(input_list, subarr_sum):
    starting_pos, curr_sum = 0, 0

    for ending_pos in range(len(input_list)):
        curr_sum += input_list[ending_pos]

        while(curr_sum > subarr_sum):
            curr_sum -= input_list[starting_pos]
            starting_pos += 1

        if (curr_sum == subarr_sum):
            return True
    else:
        return False


if __name__ == "__main__":
    input_list = [10, 20, 3, 4, 10, 20, 7, 3]
    d = 37
    print(efficient_search_subarray_sum(input_list, d))

    input_list = [1, 8, 30, 5, 20, 7]
    d = 35
    print(efficient_search_subarray_sum(input_list, d))

    input_list = [5, 10, 6, 90, 3]
    d = 93
    print(efficient_search_subarray_sum(input_list, d))
