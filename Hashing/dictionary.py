"""
Dictionary in python:
====================
collection of key-value pairs
Unordered
All keys must be distinct
values may be repeated
Uses hashing internally
"""

d = {110:"xyz", 101:"abc", 105:"bcd", 104:"abc"}
print(d)
print(d.get(101))
print(d.get(125))
print(d.get(125,"NA"))

if 125 in d:
    print(d[125])
else:
    print("NA")


d= {}
d["laptop"] = 40000
d["mobile"] = 15000
d["earphone"] = 1000
print(d)
print(d["mobile"])

d = {110:"xyz", 101:"xyz", 105:"pqr", 106:"bcd"}
d[101]= "wxy"
print(len(d))
print(d)
print(d.pop(105))
print(d)
del d[106]
d[108]="cde"
print(d.popitem())
