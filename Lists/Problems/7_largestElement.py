def maxvalue(mylist):
    if not mylist:
        return None
    else:
        max = mylist[0]
        for x in mylist:
            if x > max:
                max = x

        return max


l = [10, 5, 20, 8]
print(f"Maximum value is {maxvalue(l)}")

l = [30, 30, 20]
print(f"Maximum value is {maxvalue(l)}")

l = [40]
print(f"Maximum value is {maxvalue(l)}")

l = []
print(f"Maximum value is {maxvalue(l)}")