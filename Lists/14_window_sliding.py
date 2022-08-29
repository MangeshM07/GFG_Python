def highest_sum_subarray(mylist, d):
    if len(mylist) <= d:
        return sum(mylist)
    else:
        total=0
        for i in range(0, len(mylist)-d):
            if total < sum(mylist[i:d+i]):
                total = sum(mylist[i:d+i])
        return total

def better_highest_sum_subarray(mylist, d):
    if len(mylist) <= d:
        return sum(mylist)
    else:
        curr = 0
        for i in range(d):
            curr += mylist[i]

        res = curr
        for i in range(d, len(mylist)):
            curr = curr + mylist[i] - mylist[i-d]
            res = max(curr, res)
        return res


if __name__ == "__main__":
    input_list = [10, 20, 3, 4, 10, 20, 7, 3]
    d=3
    print(better_highest_sum_subarray(input_list, d))

    input_list = [1, 8, 30, -5, 20, 7]
    d=3
    print(better_highest_sum_subarray(input_list, d))

    input_list = []
    d=3
    print(better_highest_sum_subarray(input_list, d))

    input_list = [5, -10, 6, 90, 3]
    d=2
    print(better_highest_sum_subarray(input_list, d))
