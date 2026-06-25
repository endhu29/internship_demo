class Person:
    def display_name(self):
        name = input("Enter Name: ")
        print("Name:", name)


class Student(Person):
    def student_info(self):
        course = input("Enter Course: ")
        print("Course:", course)


class Teacher(Person):
    def teacher_info(self):
        subject = input("Enter Subject: ")
        print("Subject:", subject)


print("Student Details")
s = Student()
s.display_name()
s.student_info()

print("\nTeacher Details")
t = Teacher()
t.display_name()
t.teacher_info()    