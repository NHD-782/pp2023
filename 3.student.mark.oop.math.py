class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name, credit):
        self.id = id
        self.name = name
        self.credit = credit

class Mark:
    def __init__(self, student, course, value):
        self.student = student
        self.course = course
        self.value = value

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
                        
    def calculate_gpa(self, marks):
        total_credit = 0
        total_grade = 0
        for mark in marks:
            course = mark.course
            course_credit = int(course.credit)
            total_credit += course_credit
            grade = self.calculate_grade(mark.value)
            total_grade += grade * course_credit
        gpa = total_grade / total_credit
        return gpa
    
    def calculate_grade(self, value):
        if value >= 18:
            return 4.0
        elif value >= 15:
            return 3.0
        elif value >= 10:
            return 2.0
        elif value >= 8:
            return 1.0
        else:
            return 0.0
    
    def show_gpa(self):
        student_id = input("Enter the ID of the student you want to calculate GPA for: ")
        student_marks = [mark for mark in school.marks if mark.student.id == student_id]
        gpa = self.calculate_gpa(student_marks)
        print(f"GPA for student ID {student_id}: {gpa}")

school = School()

n = int(input("Input the number of students:\n"))
for i in range(n):
    print(f"The information of student {i+1} is: ")
    school.add_student()

m = int(input("Enter the number of courses:\n"))
for i in range(m):
    print(f"Information of course {i+1} is: ")
    school.add_course()

school.input_marks()

school.show_marks()

school.show_gpa()
