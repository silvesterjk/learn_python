# Nested classed = A class defined within another class
"""
class Outer:
    class Inner:
        pass
"""

# Benefits of nested classes:
# 1. Namespacing: Nested classes can be used to group related classes together.
# 2. Encapsulation: Nested classes can be used to hide classes that are only used by the outer class. And allows private access to the inner class.
# 3. Readability: Nested classes can be used to improve the readability of the code.

class Company:
    class Employee:
        def __init__(self, name, age, position):
            self.name = name
            self.age = age
            self.position = position

        def display_employee(self):
            return f'{self.name} is a {self.position} and is {self.age} years old.'
            
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = [] # Where employees will be stored

    def add_employee(self, name, age, position):
        new_employee = self.Employee(name, age, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.display_employee() for employee in self.employees]
        # employee.display_employee() becuase the display_employee method is in the Employee class and can be called on the employee object.
        # The employee object is an instance of the Employee class. 
    
company = Company("Google")
company.add_employee("John Doe", 30, "Software Engineer")
company.add_employee("Jane Doe", 25, "Data Scientist")
company.add_employee("Alice", 35, "Product Manager")

new_company = Company("Facebook")
new_company.add_employee("Bob", 40, "Product Manager")
new_company.add_employee("Alice", 35, "Software Engineer")
new_company.add_employee("Charlie", 25, "Data Scientist")

for index, employee in enumerate(company.list_employees()):    # Listing the employees for the company object
    print(f'{index}. {employee} Works for {company.company_name}')

print() # To create a space between the two companies

for index, employee in enumerate(new_company.list_employees()):    # Listing the employees for the new_company object
    print(f'{index}. {employee} Works for {new_company.company_name}')