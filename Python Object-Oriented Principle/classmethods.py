# Class Methods and Static Methods

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.pay = pay
        
        Employee.num_of_emps += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    # To define a class method, use @classmethod decorator
    @classmethod
    def set_raise_amt(cls, amount):
        Employee.raise_amt = amount
        
    # Alternative constructor method
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or if day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Usama', 'Hossain', 50000)
emp_1.apply_raise()
print(emp_1.pay)

emp_2 = Employee('Usama', 'Hossain', 50000)
Employee.set_raise_amt(2)
emp_2.apply_raise()
print(emp_2.pay)

# Suppose you have to parse a hyphen seperated string to get user information

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)

new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)