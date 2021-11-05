# Ways to sort list of dictionaries by values in Python – Using lambda function

# https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/?ref=rp

# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
lis = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

# using lambda and sorted() to sort dictionary by age
print("Sorting by age")
print(sorted(lis, key =lambda i:i['age']))

print('\r')

# using lambda and sorted() to sort dictionary by name
print("Sorting by name")
print(sorted(lis, key = lambda i:i['name']))

print('\r')

# using lambda and sorted() to sort dictionary by age and name
print("Sorting by name")
print(sorted(lis, key=lambda i: (i['age'], i['name'])))

print('\r')

# using lambda and sorted() to sort dictionary by age in reverse order
print("Sorting by name")
print(sorted(lis, key=lambda i: (i['age']), reverse = True))

print('\r')


