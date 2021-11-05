#  Ways to sort list of dictionaries by values in Python – Using itemgetter

# https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-itemgetter/

from operator import itemgetter

# Initialize list of dictionaries
lis = [{ "name" : "Nandini", "age" : 20},
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

# using sorted and itemgetter to print list sorted by age
print("The list printed sorting by age :")
print(sorted(lis, key=itemgetter('age')))

print('\r')

# using sorted and itemgetter to print list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(lis, key = itemgetter('age','name')))

print('\r')

# using sorted and itemgetter to print list sorted by age in descending order
print("The list printed sorting by age and name in descending order: ")
print(sorted(lis, key = itemgetter('age' ), reverse=True))

print('\r')
