l = [10, 20, 10, 30, 30, 20, 40]

length = len(set(l))
print(f"count of distinct items in list is {length}")


unique_list = list(set(l))
print(unique_list)

for i in unique_list:
    print(f"Count of {i} is {l.count(i)}")