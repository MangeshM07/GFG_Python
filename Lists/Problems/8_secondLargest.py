# def getSecMax(l):
#     if len(l) <= 1:
#         return None
#     lar = l[0]
#     slar = None
#
#     for x in l[1:]:
#         if x > lar:
#             slar = lar
#             lar = x
#         elif x!= lar:
#             if slar == None or  x > slar:
#                 slar = x
#     return slar
#
# l = [10, 20, 8, 12 ]
# print(getSecMax(l))

















def secondLargest(l):
    largest = l[0]
    second_largest = l[1]
    a=0

    if largest < second_largest:
       a = largest
       largest = second_largest
       second_largest = a

    for i in range(2, len(l)):
        if l[i] > second_largest and l[i] < largest:
            second_largest = l[i]
        return second_largest

input_list = [1, 3, 43, 63, 91]
print(secondLargest(input_list))