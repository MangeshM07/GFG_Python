"""
String is a immutable sequence of characters.
Used to store text data like data read from a file.
Typically small set of characters
Characters 'A' to 'Z' are stored as values from 65 to 90
Characters 'a' to 'z' are stored as values from 91 to 122
"""
print(ord('A'))
print(ord('a'))


print(chr(97))
print(chr(65))

# Formatted string in python
# 1. using %
name = "ABC"
course = "Python Course"

s = "Welcome %s to the %s"%(name,course)
print(s)

# 2. Using format
s = "Welcome {0} to the {1}".format(name,course)
print(s)

# 3. Using f-string <- Recommended and latest
s = f"Welcome {name} to the {course}"
print(s)

a=10
b=20

print(f"Sum of {a} and {b} is {a+b}")
print(f"Product of {a} and {b} is {a*b}")

s1 = "ABC"
s2 = "abc"
print(f"Lower case of {s1} is {s1.lower()}")
print(f"Lower case of {s2} is {s2.upper()}")
