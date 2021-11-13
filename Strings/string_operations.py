s1 = "geeksforgeeks"
s2 = "geeks"

print(s2 in s2)
print(s1 in s2)

s3 = s1+s2
print(s3)

print(s1.index(s2))
print(s1.rindex(s2))
print(s1.index(s2,0,13))
print(s1.index(s2,1,13))
# ValueError --> if searched string is not present

print(len(s2))
print(s2.upper())
print(s2.lower())
print(s2.isupper())
print(s2.islower())

print(s1.startswith("geeks"))
print(s1.endswith("geeks"))
print(s1.startswith("geeks",1))
print(s1.endswith("geeks",8, len(s1)))

s4 = "Geeks For Geeks"
print(s4.split())

s5 = "Geeks,For,Geeks"
print(s5.split(","))

l = ['Geeks', 'For', 'Geeks']
print(" ".join(l))
print(",".join(l))

s6 = "----geeksforgeeks---"
print(s6.strip("-"))
print(s6.lstrip("-"))
print(s6.rstrip("-"))


print(s1.find(s2))
print(s1.find("gfg"))
print(s1.find(s2, 1, len(s1)+1))
