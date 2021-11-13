txt = "geeks for geeks"
patt = "geeks"

pos = txt.find(patt)

while pos >= 0:
    print(pos)
    pos = txt.find(patt, pos+1)