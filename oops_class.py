class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print("Name:", self.name)

    def increment_salary(self):
        self.salary += 5000
        print("Salary Increased")

    def show_salary(self):
        print("Salary:", self.salary)

    def department_details(self):
        print("Department:", self.department)


name = input("Enter Employee Name: ")
dept = input("Enter Department: ")
salary = int(input("Enter Salary: "))

emp = Employee(name, dept, salary)

emp.display()
emp.department_details()
emp.increment_salary()
emp.show_salary()