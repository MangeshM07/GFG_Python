# li = [9,1,8,2,7,3,6,4,5]
# s_li = sorted(li, reverse=True)
#
# print("Sorted list :\t", s_li)
#
# li.sort(reverse=True)
# print("Original list :\t", li)

# tup = (9,1,8,2,7,3,6,4,5)
# s_tup = sorted(tup)
#
# #cannot use sort method on tuple
# print("Sorted tuple :\t", s_tup)
# print("Original tuple :\t", tup)

#
# di = {"name":"John Doe", "Job":"Programming", "Age":"29", "OS":"Linux"}
# s_di = sorted(di)
#
# print("Sorted dictionary :\t", s_di)
# print("Original Dictionary:", di)

# li = [-6,-5,-4,1,2,3,-9]
# # sort based on absolute value
# s_li = sorted(li, key=abs)
#
# print("Sorted list :\t", s_li)
#
# print("Original list :\t", li)

from operator import attrgetter
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"({self.name},{self.age},{self.salary})"


e1 = Employee("Carl", 37, 70000)
e2 = Employee("Sarah", 29, 80000)
e3 = Employee("John", 43, 90000)

employees = [e1, e2, e3]

# s_employees = sorted(employees, key=lambda e: e.salary)
s_employees = sorted(employees, key=attrgetter('age')) #Another way
print("Sorted employees: \t", s_employees)
print("Original employees: \t", employees)