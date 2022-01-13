"""
Time complexity for iterative and recursive binary search is O(log n).
While space complexity for iterative solution is O(1) while recursive is O(log n)
So iterative solution should be preferred over recursive solution in Binary search

"""

def recursive_bSearch(input_list, search_value, low, high):
    if low > high:
        return -1

    mid = (low+high)//2

    if input_list[mid] == search_value:
        return mid
    elif input_list[mid] > search_value:
        return recursive_bSearch(input_list, search_value, low, mid-1)
    else:
        return recursive_bSearch(input_list, search_value, mid+1, high)

l = [10, 20, 30, 40, 50, 60]
low=0
high=len(l)-1

print(30, recursive_bSearch(l, 30, low, high))
print(20, recursive_bSearch(l, 20, low, high))
print(10, recursive_bSearch(l, 10, low, high))
print(60, recursive_bSearch(l, 60, low, high))
print(40, recursive_bSearch(l, 40, low, high))
print(55, recursive_bSearch(l, 55, low, high))
print(-50, recursive_bSearch(l, -50, low, high))