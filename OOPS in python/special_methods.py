# Python (Magic/Dunder) Methods
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbWFybUhBbFd0Q25PUzVnMVJBdDdjaGtJVVg5Z3xBQ3Jtc0tsYUE5X2Ixb0NRZ0hiU1ZoUFFSNHQ1YlRfMGFDdVA1WU9vcUhsVDAxZ2xaX3E2SW5ycUx6MERSQ1R3Z2UwVTlZTjhwaXU2X3RrOEVBSl9HT05MdE9zS2ZPVnhIQkF3QkQzRDJZSFluNlFyZFBHR3g2QQ&q=https%3A%2F%2Fdocs.python.org%2F3%2Freference%2Fdatamodel.html%23special-method-names
# https://docs.python.org/3/reference/datamodel.html#special-method-names

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

    def __repr__(self):
        return "Employee('{}', '{}', '{}'".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Tom", "Cruise", 80000)
emp_2 = Employee("Will", "Smith", 76000)

print(emp_1) # Before repr method --> output was : <__main__.Employee object at 0x014B8850>

print(emp_1.__repr__())
print(emp_1.__str__())

print(1+3)
print(int.__add__(1, 3))

print('a'+'b')
print(str.__add__('a', 'b'))

print(emp_1 + emp_2)

print(len('test'))
print('test'.__len__())

print(len(emp_1))
