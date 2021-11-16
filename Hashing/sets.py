"""
Sets in Python
==============
Distinct elements
unordered
No indexing
union, intersection, set difference, etc are fast
uses hashing internally

"""
s1 = {10, 20, 30}
print(type(s1))
print(s1)

s2 = set([20, 30, 40])
print(s2)

s3 = {}
print(type(s3))

s4 = set()
print(type(s4))
print(s4)

s = {10, 20}
s.add(30)
print(s)

s.add(30)
print(s)

s.update([40, 50])
print(s)

s.update([60, 70], [80, 90])
print(s)

s.discard(30)  # discard function does not throws error if provided value not in the set
print(s)

s.remove(20)  # remove raises an error if data not found
print(s)

s.clear()  # all entries are removed , making set as empty
print(s)

s.add(50)
print(s)

del s  # deletes set itself

s = {10, 20, 30, 40}
print(len(s))

print(20 in s)  # IN operator is fater in sets as compared to lists bcoz it uses hashing internally
print(50 in s)

# Operations on two sets
s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}
print(s1 | s2)  # same as s1.union(s2)
print(s1 & s2)  # same as s1.intersection(s2)
print(s1 - s2)  # same as s1.difference(s2)
print(s1 ^ s2)  # same as s1.symmetric_difference(s2)

s1 = {2, 4, 6, 8}
s2 = {4,8}
print(s1.isdisjoint(s2))
print(s1 <= s2)  # same as print(s1.issubset(s2))
print(s1 < s2)   # checks s1 is proper subset of s2
print(s1 >= s2)  # same as s2.issubset(s1))
print(s1 > s2)  # checks s2 is proper subset of s1
