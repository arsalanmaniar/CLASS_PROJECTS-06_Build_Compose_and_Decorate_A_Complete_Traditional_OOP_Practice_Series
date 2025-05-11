class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn  # Private attribute

    def get__ssn(self):
        return self.__ssn
    
    def set_salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            print("Invalid salary. Salary must be positive.")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")

class Manager(Employee):
    def __init__(self, name, salary, ssn, department):
        super().__init__(name, salary, ssn)
        self.department = department

    def show_manager_info(self):
        print(f"Manager Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Protected Salary: {self._salary}")
        print(f"Accessing SSN via getter command: {self.get__ssn()}")

m = Manager("Alice", 80000, "123-45-6789", "HR")
m.show_manager_info()
m.set_salary(90000)
print("Updated Salary: ", m._salary)

# print(m.__ssn)
print("Private SSN via managed:", m._Employee__ssn)  # This will raise an error