'''
A given string can be a palindrome if there is
at most one character with odd frequency.
   abba, acbccab, aaaabbbbddd
else
    false
    abcc, ab, aaabbcdd, .....
'''


def palindrome_check(input_string):
    distinct_chars = set(input_string)
    odd_count = 0
    for i in distinct_chars:
        char_count = input_string.count(i)
        if char_count%2 != 0:
            odd_count += 1

    if odd_count <= 1:
        return True
    else:
        return False


def sub_array_sum_zero(l):
    n = len(l)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if sum(l[i:j]) == 0:
                return True
    return False


def sub_array_sum_zero_efficient(l):
    prefix_sum = 0
    set_container = set()

    for i in range(len(l)):
        prefix_sum += l[i]

        if prefix_sum == 0 or prefix_sum in set_container:
            return True

        set_container.add(prefix_sum)

    return False


# l = [4, 3, -2, 1, 1]
# print(sub_array_sum_zero_efficient(l))

print(palindrome_check("abbcdd"))