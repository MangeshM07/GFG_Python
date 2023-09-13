def odd_even_separate(arr):
    even_list = []
    odd_list = []
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            even_list.append(arr[i])
        else:
            odd_list.append(arr[i])

    print(even_list)
    print(odd_list)

input_list = [8, 12, 15, 9, 3, 11, 26, 23]
odd_even_separate(input_list)