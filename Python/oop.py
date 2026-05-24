class SchoolId:
    def __init__(self, name, grade, student_id, address, number):
        self.name = name
        self.grade = grade
        self.student_id = student_id
        self.address = address
        self.number = number

    def display(self):
        print("----- Student Details -----")
        print(f"Name       : {self.name}")
        print(f"Grade      : {self.grade}")
        print(f"Student ID : {self.student_id}")
        print(f"Address    : {self.address}")
        print(f"Number     : {self.number}")

student1 = SchoolId("Alice", "10th", "S12345", "456 Oak Ave", "555-1234")
student1.display()

student2 = SchoolId("Bob", "11th", "S67890", "789 Pine Rd", "555-5678")
student2.display()

student3 = SchoolId("Charlie", "12th", "S54321", "321 Maple St", "555-9012")
student3.display()

