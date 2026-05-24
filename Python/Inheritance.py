# single inheritance

class School:
        def __init__(self, name, location):
            self.name = name
            self.location = location
    
        def displaySchoolData(self):
            print(f"School Name: {self.name}")
            print(f"Location: {self.location}")

class Student(School):
    def __init__(self, name, location, studentName, grade, rollNumber):
        super().__init__(name, location)
        self.studentName = studentName
        self.grade = grade
        self.rollNumber = rollNumber

    def displayStudentData(self):
        print(f"Student Name: {self.studentName}")
        print(f"Grade: {self.grade}")
        print(f"Roll Number: {self.rollNumber}")

student1 = Student("Greenwood High", "New York", "Alice", "10th", "S12345")
print(f"School Name: {student1.name}")
print(f"Location: {student1.location}")
student1.displayStudentData()

# multiple inheritance 

class School:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    
    def displaySchoolData(self):
        print(f"School Name: {self.name}")
        print(f"Location: {self.location}")

class Teacher:
    def __init__(self, teacherName, subject):
        self.teacherName = teacherName
        self.subject = subject

    def displayTeacherData(self):
        print(f"Teacher Name: {self.teacherName}")
        print(f"Subject: {self.subject}")

class Student(School, Teacher):
    def __init__(self, name, location, teacherName, subject, studentName, grade, rollNumber):
        School.__init__(self, name, location)
        Teacher.__init__(self, teacherName, subject)
        self.studentName = studentName
        self.grade = grade
        self.rollNumber = rollNumber

    def displayStudentData(self):
        self.displaySchoolData()
        self.displayTeacherData()
        print(f"Student Name: {self.studentName}")
        print(f"Grade: {self.grade}")
        print(f"Roll Number: {self.rollNumber}")

student1 = Student("Greenwood High", "New York", "Mr. Smith", "Math", "Alice", "10th", "S12345")
student1.displayStudentData()


# multilevel inheritance


class GrandFather:
    def __init__(self, grandFatherName):
        self.grandFatherName = grandFatherName

    def displayGrandFather(self):
        print(f"GrandFather Name: {self.grandFatherName}")

class Father(GrandFather):
    def __init__(self, grandFatherName, fatherName):
        super().__init__(grandFatherName)
        self.fatherName = fatherName

    def displayFather(self):
        print(f"Father Name: {self.fatherName}")

class Son(Father):
    def __init__(self, grandFatherName, fatherName, sonName):
        super().__init__(grandFatherName, fatherName)
        self.sonName = sonName

    def displaySon(self):
        self.displayGrandFather()
        self.displayFather()
        print(f"Son Name: {self.sonName}")

son1 = Son("John", "Michael", "David")
son1.displaySon()

# hierarchical inheritance

class School:
    def __init__(self,name,location):
        self.name = name
        self.location = location
    
    def displaySchool(self):
        print(f"School Name: {self.name}")
        print(f"Location: {self.location}")


class Student(School):
    def __init__(self, name, location, studentName, grade, rollNumber):
        super().__init__(name, location)
        self.studentName = studentName
        self.grade = grade
        self.rollNumber = rollNumber

    def displayStudent(self):
        self.displaySchool()
        print(f"Student Name: {self.studentName}")
        print(f"Grade: {self.grade}")
        print(f"Roll Number: {self.rollNumber}")


class Teacher(Student):
    def __init__(self, name, location, studentName, grade, rollNumber, teacherName, subject):
        super().__init__(name, location, studentName, grade, rollNumber)
        self.teacherName = teacherName
        self.subject = subject

    def displayTeacher(self):
        self.displayStudent()
        print(f"Teacher Name: {self.teacherName}")
        print(f"Subject: {self.subject}")


teacher1 = Teacher("Greenwood High", "New York", "Alice", "10th", "S12345", "Mr. Smith", "Math")
teacher1.displayTeacher()