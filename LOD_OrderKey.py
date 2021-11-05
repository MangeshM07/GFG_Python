# Given list of dictionaries, convert to ordered key dictionary with each key contained dictionary as its nested value.
#
# Input : test_list = [{“Gfg” : 3, 4 : 9}, {“is”: 8, “Good” : 2}]
# Output : {0: {‘Gfg’: 3, 4: 9}, 1: {‘is’: 8, ‘Good’: 2}}
# Explanation : List converted to dictionary with index keys.
#
# Input : test_list = [{“is”: 8, “Good” : 2}]
# Output : {1: {‘is’: 8, ‘Good’: 2}}
# Explanation : List converted to dictionary with index keys, just one row.

    # Method #1 : Using loop + enumerate()
    #
    # # This is brute way in which this task can be performed.
    # # In this, we iterate through the index and value together using enumerate and create custom required dictionary.

# Python3 code to demonstrate working of
# Convert Dictionaries List to Order Key Nested dictionaries
# Using loop + enumerate()

# initializing lists
membership = [
    {'id':1, 'startYear':1880, 'endYear':1930},
    {'id':2, 'startYear':1910, 'endYear':1945},
    {'id':3, 'startYear':1890, 'endYear':1970},
    {'id':4, 'startYear':1925, 'endYear':1999},
    {'id':5, 'startYear':1976, 'endYear':2021}
]

# printing the original list
print("The original list : " +str(membership))
print('\n')

# using enumerate() to extract key to map with dict values
res = dict()
for index,val in enumerate(membership):
    res[index] = val

print("The constructed dictionary :" + str(res))
print('\n\n')
# Method #2 : Using dictionary comprehension + enumerate()
#
# This is similar to above method, the only difference is that dictionary comprehension is used instead of loop to perform task of encapsulation.

res = { index: val for index,val in enumerate(membership)}
print(res)