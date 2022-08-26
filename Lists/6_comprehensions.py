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

l9 = ["geeks", "for", "geeks", "gfg", "ide"]
l10 = [x.upper() for x in l9 if x.startswith("g")]
print(l10)

# Set Comprehensions
l11 = [10,20,3,4,10,20,7,3]
s1 = {x for x in l11 if x%2==0}
s2 = {x for x in l11 if x%2!=0}
print(s1)
print(s2)

# Dictionary comprehension
l12 = [1,3,4,2,5]
d1 = {x:x**3 for x in l12}
print(d1)

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)

l13 = [101,102,103]
l14 = ["gfg", "ide", "courses"]
d3 = {l13[i]:l14[i] for i in range(len(l13))}
print(d3)

# Better way to create dictionary from 2 lists
d4 = dict(zip(l13, l14))
print(d4)

# Inverting a dictionary (Key becomes value and value becomes key)
d5 = {101: 'gfg', 102: 'ide', 103: 'courses'}
d6 = {v:k for (k,v) in d5.items()}
print(d6)


# given a list , find list of odd and even elements
lst = [1,3,6,2,8,43,63,76,91]
even_list = [ item for item in lst if item%2==0 ]
odd_list = [ item for item in lst if item%2!=0 ]
print(even_list)
print(odd_list)