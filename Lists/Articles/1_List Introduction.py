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