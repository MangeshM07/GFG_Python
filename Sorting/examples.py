l1 = [5, 10, 15, 1]
l1.sort()
print(l1)

l2 = [1, 5, 2, 10]
l2.sort(reverse=True)
print(l2)

l3 = ["gfg", "ide", "courses"]
l3.sort()
print(l3)


def myFun(s):
    return len(s)


l = ["gfg", "ide", "courses"]
l.sort(key=myFun)
print(l)

l = ["gfg", "ide", "courses"]
l.sort(key=myFun, reverse=True)
print(l)

# ********************************************************************#
print("# ********************************************************************#")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def myFun(p):
    return p.x


l = [Point(1, 5), Point(10, 5), Point(1, 8)]
l.sort(key=myFun)
for i in l:
    print(i.x, i.y)

# ********************************************************************#
print("# ********************************************************************#")
# Using __lt__ method

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x


l = [Point(1, 5), Point(10, 5), Point(1, 8)]
l.sort()
for i in l:
    print(i.x, i.y)


# ********************************************************************#
print("# ********************************************************************#")
# Using __lt__ method and adding additional logic

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        if self.x == other.y:
            return self.y < other.y
        else:
            return self.x < other.x


l = [Point(1, 15), Point(10, 5), Point(1, 8)]
l.sort()
for i in l:
    print(i.x, i.y)