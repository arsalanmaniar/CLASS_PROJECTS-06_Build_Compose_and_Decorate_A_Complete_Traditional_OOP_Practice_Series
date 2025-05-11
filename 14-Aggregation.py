class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to an existing employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.show()  # Call employee's method

# Create Employee independently
emp1 = Employee("Alice")

# Pass employee to department (aggregation)
dept = Department("HR", emp1)

# Show department and employee details
dept.show_details()
