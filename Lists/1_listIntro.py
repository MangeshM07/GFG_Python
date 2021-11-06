lst = [10,20,30,40,50]

print(lst)
print(lst[3])
print(lst[-1])
print(lst[-2])

# add elements in list
lst.append(30)
print(lst)

lst.insert(1,15)
print(lst)

print(15 in lst)

print(lst.count(30))

print(lst.index(30))

print(lst.index(30,4,7))  # index(value, Starting Position, Ending Position(it is exclusive))

# Remove elements from list

l = [10,20,30,40,50,60,70,80]

l.remove(20)
print(l)

print(l.pop())
print(l)

print(l.pop(2))
print(l)

del l[1]
print(l)

del l[0:2]
print(l)

# More general purpose functions
lst = [10,20,30,40,50]

print(max(lst))
print(min(lst))
print(sum(lst))
lst.reverse()
print(lst)

lst.sort()
print(lst)


