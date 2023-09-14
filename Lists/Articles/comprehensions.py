# Constructing output list WITHOUT
# Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_list = []

# Using loop for constructing output list
for var in input_list:
	if var % 2 == 0:
		output_list.append(var)

print("Output List using for loop:", output_list)

# Using List comprehensions
# for constructing output list

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]


list_using_comp = [var for var in input_list if var % 2 == 0]

print("Output List using list comprehensions:",	list_using_comp)

input_list = [1, 2, 3, 4, 5, 6, 7]

output_dict = {}

# Using loop for constructing output dictionary
for var in input_list:
	if var % 2 != 0:
		output_dict[var] = var**3

print("Output Dictionary using for loop:",	output_dict )


# Using Dictionary comprehensions
# for constructing output dictionary

input_list = [1,2,3,4,5,6,7]

dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:",	dict_using_comp)

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = set()

# Using loop for constructing output set
for var in input_list:
	if var % 2 == 0:
		output_set.add(var)

print("Output Set using for loop:", output_set)

# Using Set comprehensions
# for constructing output set

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",set_using_comp)

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]

output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end = ' ')

for var in output_gen:
	print(var, end = ' ')