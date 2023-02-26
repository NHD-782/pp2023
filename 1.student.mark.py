# Input the number of students
def numberStudent(n):
    n = int(input("Input the number of students:\n"))
    for i in range(1, n+1, 1):
        print("The information of student {0} is: ".format(i))
        listStudents.append(studentInformation())
    return listStudents

# Input the number of courses
def numberCourse(m):
    m = int(input("Enter the number of courses:\n"))
    for i in range(1, m+1, 1):
        print("Information of course {0} is: ".format(i))
        listCourses.append(courseInformation())
    return listCourses

# Input student information
def studentInformation():
    id = input("Student ID: ")
    name = input("Student Name: ")
    DoB = input("Student DoB: ")
    return {"id": id, "name": name, "DoB": DoB}

# Input course information
def courseInformation():
    id = input("Course ID: ")
    name = input("Course Name: ")
    return {"id": id, "name": name}

# Input marks for each student in each course
def inputMarks(listStudents, listCourses):
    print("Marks for each student in each course:")
    for i in range(len(listCourses)):
        print("{0}: ".format(listCourses[i]["name"]))
        for j in range(len(listStudents)):
            mark = int(input("{0} mark: ".format(listStudents[j]["name"])))
            marks.append(mark)
    return marks

# Show marks for a selected course
def showMarks(listStudents, listCourses, idCourse):
    idCourse = input("Choose the ID course you want to show marks for: ")
    for i in range(len(listCourses)):
        if idCourse == listCourses[i]["id"]:
            print("Marks for ID {0}({1}):".format(idCourse, listCourses[i]["name"]))
            for j in range(len(listStudents)):
                mark = marks[i*len(listStudents) + j]
                print("{0}: {1}".format(listStudents[j]["name"], mark))
    return

# Initialize variables
n = 0
m = 0

id = ""
name = ""
DoB = ""
nameCourse = ""

marks = []
listStudents = []
listCourses = []

# Call the functions
numberStudent(n)
print("------------------------------")
numberCourse(m)
print("------------------------------")
inputMarks(listStudents, listCourses)
print("------------------------------")
showMarks(listStudents, listCourses, nameCourse)
