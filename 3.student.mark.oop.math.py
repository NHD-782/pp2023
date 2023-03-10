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
        
    def show_all_student(self):
        print("Students:")
        print("| {0: <10} | {1: <20} | {2: <15} |".format('ID', 'Name', 'DoB'))
        print("-" * 50)
        for student in self.students:
            print("| {0: <10} | {1: <20} | {2: <15} |".format(student.id, student.name, student.dob))
        print()

    def add_course(self):
        id = input("Course ID: ")
        name = input("Course Name: ")
        credit = input("Course credit: ")
        course = Course(id, name, credit)
        self.courses.append(course)
        
    def show_all_courses(self):
        print("Courses:")
        print("| {0: <10} | {1: <20} | {2: <15} |".format('ID', 'Name', 'Credit'))
        print("-" * 50)
        for course in self.courses:
            print("| {0: <10} | {1: <20} | {2: <15} |".format(course.id, course.name, course.credit))
        print()

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
                        
    def calculate_gpa(self, student):
        total_credits = 0
        total_grade_points = 0
        for mark in self.marks:
            if mark.student == student:
                course = mark.course
                credit = int(course.credit)
                grade_point = self.grade(mark.value)
                total_credits += credit
                total_grade_points += credit * grade_point
        if total_credits > 0:
            gpa = total_grade_points / total_credits
        else:
            gpa = 0
        return gpa

    def grade(self, mark):
        if mark >= 0:
            return mark

    def show_gpa(self):
        print("GPA for each student:")
        for student in self.students:
            gpa = self.calculate_gpa(student)
            print(f"{student.name}: {gpa:.2f}")
            
    def show_all_mark_GPA(self):
        print("Marks and GPA for each students:")
        print("| {0: <20} | {1: <20} | {2: <10} | {3: <5} |".format('Student Name', 'Course Name', 'Value', 'GPA'))
        print("-" * 70)
        for mark in self.marks:
            gpa = self.calculate_gpa(mark.student)
            print("| {0: <20} | {1: <20} | {2: <10} | {3: <5.2f} |".format(mark.student.name, mark.course.name, mark.value, gpa))

school = School()

# Input the number of students
n = int(input("Input the number of students:\n"))
for i in range(n):
    print(f"The information of student {i+1} is: ")
    school.add_student()
    
school.show_all_student() # Print all the students input from keyboard

# Input the number of courses
m = int(input("Enter the number of courses:\n"))
for i in range(m):
    print(f"Information of course {i+1} is: ")
    school.add_course()
    
school.show_all_courses() # Print all the courses input from keyboard

school.input_marks() # Input marks for each student in each course

school.show_all_mark_GPA() # Print all the marks and GPA for each student input from keyboard
