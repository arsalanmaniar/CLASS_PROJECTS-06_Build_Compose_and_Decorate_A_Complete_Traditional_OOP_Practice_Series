class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Students Marks: {self.marks}")

student1 = Student("Arsalan", 90)
student1.display()