def oddEvenList(mylist):
    oddlist = []
    evenlist = []
    for i in mylist:
        if i % 2 == 0:
            evenlist.append(i)
        else:
            oddlist.append(i)

    return evenlist, oddlist


l = [10, 41, 30, 15, 80]
even, odd = oddEvenList(l)
print("Even list is " + str(even))
print("Odd list is " + str(odd))

l = [10, 30, 40]
even, odd = oddEvenList(l)
print("Even list is " + str(even))
print("Odd list is " + str(odd))
