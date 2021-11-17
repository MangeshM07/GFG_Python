class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def email(self):
        return f"{self.first}.{self.last}@email.com"

    def hike(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        # Employee.__init__(self, first, last, pay) # one way to initialize
        super().__init__(first, last, pay) # Most used way to initialize in subclass
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


emp_1 = Employee("John", "Hartley", 50000)
print(emp_1.pay)
emp_1.hike()
print(emp_1.pay)

emp_2 = Employee.from_string("Johnny-Joshua-4000000")
print(emp_2.fullname())
print(emp_2.email())

# print(help(Developer)) -- Get all info of this class
dev_1 = Developer("Vikram", "Pandit", 50000, "Python")
print(dev_1.email())
print(dev_1.prog_lang)

manager_1 = Manager("Chris", "Tango", 90000, [emp_1])
manager_1.add_employee(emp_2)
manager_1.print_emps()
manager_1.remove_employee(emp_1)
print("After removal of employee")
manager_1.print_emps()

print(isinstance(manager_1, Employee))
print(issubclass(Developer, Manager))