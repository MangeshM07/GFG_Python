Var = ['Geeks', 'for', 'geeks']
print(Var)
print(type(Var))


# Python program to demonstrate
# Creation of List
List= []
print('Blank List:')
print(List)

# Creating a list of numbers
List = [10, 20 , 30 , 30]
print('\nList of numbers')
print(List)

# Creating a list of strings and accessing using index
List = ["Geeks", "for", "geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])

# Complexities for Creating Lists
# Time  Complexity: O(1)
# Space Complexity: O(n)

# Example 2:  Creating a list with multiple distinct or duplicate elements
List = [1, 2, 4, 4, 3, 3, 6, 5]
print("\n List with the use of numbers: ")
print(List)

List = [1, 2, "Geeks", "for", 4, 5, "geeks"]
print(List)

# Example : Accessing elements from list
# Python program to demonstrate accessing element from a multi dimensional list
List = [["Geeks", "For"], ["Geeks"]]
print(List[0][1])
print(List[1][0])

# Negative indexing
List = [1, 2, "Geeks", "for", 4, 5, "geeks"]
print(List[-1])
print(List[-3])

# Complexities for Accessing elements in a Lists:
# Time Complexity: O(1)
# Space Complexity: O(1)

# getting size of python list
List1 = []
print(len(List1))

List2 = [10, 20, 14]
print(len(List2))

# Taking Input of a Python List
# We can take the input of a list of elements as string, integer, float, etc. But the default one is a string.

string = input("Enter elements (space separated) :")

lst = string.split()
print("The list is:", lst)

# input size of the list
n = int(input("Enter the size of list : "))
# store integrs in a list using map,  split and strip functions
lst = list(map(int, input("Enter the integer elements: ").strip().split()))[:n]

print('The list is :', lst)

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

# Complexities for Adding elements in a Lists(append() method):
# Time Complexity: O(1)
# Space Complexity: O(1)

# Method 2: Using insert() method
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List)

# Complexities for Adding elements in a Lists(insert() method):
# Time Complexity: O(n)
# Space Complexity: O(1)

# Method 3: Using extend() method
"""
Other than append() and insert() methods, there's one more method for the Addition of elements,
 extend(),  this method is used to add multiple elements at the same time at the end of the list."""
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements to the List at the end (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)

# Complexities for Adding elements in a Lists(extend() method):
# Time Complexity: O(n)
# Space Complexity: O(1)

# Reversing a list
# A list can be reversed by using the reverse() method in Python.

List.reverse()
print(List)


# Removing Elements from the List

# Method 1: Using remove() method

List.remove(3)
List.remove('Always')
print("\nList after Removal of two elements: ")
print(List)

# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)

# Complexities for Deleting elements in a Lists(remove() method):
# Time Complexity: O(n)
# Space Complexity: O(1)


# Method 2: Using pop() method

List = [1, 2, 3, 4, 5]

# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)

"""
Complexities for Deleting elements in a Lists(pop() method):
    Time Complexity: O(1) / O(n)(O(1) for removing the last element, O(n) for removing the first and middle elements)
    Space Complexity: O(1)
"""
