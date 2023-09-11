def revlist(mylist):
    return mylist[::-1]


l = [10, 20, 30, 40, 50]
print(revlist(l))
print(l[:])

l2= l[:]

t1 = (10, 20, 30)
t2 = t1[:]

s1 = "geeks"
s2 = s1[:]

print(l in l2)
print(t1 in t2)
print(s1 in s2)
