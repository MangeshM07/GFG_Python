def first_Recurring_Character(array):
    characters_dictionary ={}

    for element in array:
        if element in characters_dictionary:
            return element
        else:
            characters_dictionary[element]="True"

    return "No recurring character"

lst = [5,6,4,2,7,6]
print(first_Recurring_Character(lst))

lst = [2,5,1,2,3,5,1,2,4]
print(first_Recurring_Character(lst))

lst = [2,3,3,2,4,5]
print(first_Recurring_Character(lst))