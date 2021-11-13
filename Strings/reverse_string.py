def reverse_string(input_string):
    rev = ""
    for i in input_string:
        rev = i+rev
    print(rev)


input = "Geek"
print(reverse_string(input))
print(input[::-1])