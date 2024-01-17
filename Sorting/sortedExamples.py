# Sorted() in Python
# ===================
#
#
# --> Works for any iterables(List, Tuple, Dictionary, String, Set, etc)
# --> Returns a n ew list with sorted items
# --> parameters like reverse and key work same way as sort()
#
# */
from builtins import print

l = [10, 20, 14]
ls = sorted(l)

print(l)
print(ls)

l = [10, -15, -2, 1]
ls = sorted(l, key = abs, reverse=True)

nls = sorted(l, reverse=False)
print(nls)