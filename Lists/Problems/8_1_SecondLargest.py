def secondLargest(arr):
    if len(arr) < 2:
        return "Number of elements in the list should be at least 2"

    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "No second largest element found"
    else:
        return second_largest

my_list = [12, 45, 2, 41, 31, 10, 8]
result = secondLargest(my_list)
print("Second largest element:", result)
