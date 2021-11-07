# List comprehension provides you with a shortcut syntax to create a list from another iterable


l1 = [x for x in range(11) if x % 2 == 0]
print(l1)

l2 = [x for x in range(11) if x % 2 != 0]
print(l2)

my_list = [8, 100, 20, 40, 3, 7]
input_value = 10
l3 = [x for x in my_list if x < input_value]
print(l3)

l4 = [10, 41, 30, 15, 80]
even_list = [x for x in l4 if x % 2 == 0]
odd_list = [x for x in l4 if x % 2 != 0]
print(even_list)
print(odd_list)

s = "geeksforgeeks"
l5 = [x for x in s if x in "aeiou"]
print(l5)

l6 = ["geeks", "ide", "courses", "gfg"]
l7 = [x for x in l6 if x.startswith("g")]
print(l7)

l8 = [x*2 for x in range(6)]
print(l8)

