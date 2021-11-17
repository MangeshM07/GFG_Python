# More efficient solution
from collections import Counter


def ispalPos(mystr):
    cnt = Counter(mystr)
    print(cnt)

    odd = 0
    for freq in cnt.values():
        if freq % 2 != 0:
            odd = odd + 1
            if odd > 1:
                return False
    return True


def isPalindromePossible(mystr):
    distinct_chars = set(mystr)
    odd_count = 0
    for i in distinct_chars:
        if mystr.count(i) % 2 == 1:
            odd_count += 1

    if odd_count > 1:
        return False
    else:
        return True


input_str = 'abcc'
print(isPalindromePossible(input_str))

input_str = 'geeksgeeks'
print(ispalPos(input_str))

input_str = 'abaaac'
print(ispalPos(input_str))
