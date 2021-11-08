def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None

    for x in l[1:]:
        if x > lar:
            slar = lar
            lar = x
        elif x!= lar:
            if slar == None or  x > slar:
                slar = x
    return slar

l = [10, 20, 8, 12 ]
print(getSecMax(l))
