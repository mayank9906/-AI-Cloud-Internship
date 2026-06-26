class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("\n===== Student Details =====")
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Course :", self.course)


# Creating Object

student1 = Student("Mayank", 20, "BCA")

student1.display()