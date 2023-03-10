# Creat class Student
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

# Creat class Course
class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

# Creat class Mark
class Mark:
    def __init__(self, student, course, value):
        self.student = student
        self.course = course
        self.value = value

# Creat class School
class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def add_student(self):
        id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Student DoB: ")
        student = Student(id, name, dob)
        self.students.append(student)

    def add_course(self):
        id = input("Course ID: ")
        name = input("Course Name: ")
        credit = input("Course credit: ")
        course = Course(id, name, credit)
        self.courses.append(course)

    def input_marks(self):
        print("Marks for each student in each course:")
        for course in self.courses:
            print(f"{course.name}: ")
            for student in self.students:
                value = int(input(f"{student.name} mark: "))
                mark = Mark(student, course, value)
                self.marks.append(mark)

    def show_marks(self):
        id_course = input("Choose the ID course you want to show marks for: ")
        for course in self.courses:
            if course.id == id_course:
                print(f"Marks for ID {course.id}({course.name}):")
                for mark in self.marks:
                    if mark.course == course:
                        print(f"{mark.student.name}: {mark.value}")


school = School()

# Input the number of students
n = int(input("Input the number of students:\n"))
for i in range(n):
    print(f"The information of student {i+1} is: ")
    school.add_student()

# Input the number of courses
m = int(input("Input the number of courses:\n"))
for i in range(m):
    print(f"Information of course {i+1} is: ")
    school.add_course()

school.input_marks() # Input marks for each student in each course

school.show_marks() # Print marks for each student in each course on the screen
