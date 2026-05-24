from abc import ABC, abstractmethod


# Abstract Class
class School(ABC):

    def __init__(self, schoolName, location):
        self.schoolName = schoolName
        self.location = location

    # Normal Method
    def displaySchoolData(self):
        print(f"School Name: {self.schoolName}")
        print(f"Location: {self.location}")

    # Abstract Method
    @abstractmethod
    def displayRole(self):
        pass


# Child Class
class Student(School):

    def __init__(self, schoolName, location, studentName, grade, rollNumber):
        super().__init__(schoolName, location)

        self.studentName = studentName
        self.grade = grade
        self.rollNumber = rollNumber

    # Implementing Abstract Method
    def displayRole(self):
        print("Role: Student")

    # Student Method
    def displayStudentData(self):
        self.displaySchoolData()
        self.displayRole()

        print(f"Student Name: {self.studentName}")
        print(f"Grade: {self.grade}")
        print(f"Roll Number: {self.rollNumber}")


# Object Creation
student1 = Student(
    "Greenwood High",
    "New York",
    "Alice",
    "10th",
    "S12345"
)

student1.displayStudentData()