# Python OOP

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee("Tom", "Cruise", 80000)
emp_2 = Employee("Will", "Smith", 76000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(Employee.fullname(emp_2))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(emp_1.raise_amount)
print(Employee.raise_amount)

# calling class method 
Employee.set_raise_amt(1.05)

print(emp_1.raise_amount)
print(Employee.raise_amount)
#
# print(emp_1.__dict__)
# print(Employee.__dict__)

print(Employee.num_of_emps)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-smith-40000"
emp_str_3 = "Glenn-Maxwell-60000"

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())
print(new_emp_1.email)

