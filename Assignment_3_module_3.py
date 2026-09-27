
class Student:
    def __init__(self, name, student_id, email, age, department, marks):
        self.name = name
        self.student_id = student_id
        self.__email = email       # Encapsulation
        self.age = age
        self.department = department
        self.__marks = marks       # Encapsulation

    # Getter for private email
    def get_email(self):
        return self.__email

    # Getter for private marks
    def get_marks(self):
        return self.__marks

    # Update marks
    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks. Marks must be between 0 and 100.")

    # Parent method
    def display_info(self):
        print("\n--- Student Information ---")
        print(f"Name       : {self.name}")
        print(f"Student ID : {self.student_id}")
        print(f"Email      : {self.__email}")
        print(f"Age        : {self.age}")
        print(f"Department : {self.department}")
        print(f"Marks      : {self.__marks}")

    # Result calculation
    def calculate_result(self):
        marks = self.__marks

        if marks >= 80:
            grade = "A+"
        elif marks >= 70:
            grade = "A"
        elif marks >= 60:
            grade = "A-"
        elif marks >= 50:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        elif marks >= 33:
            grade = "D"
        else:
            grade = "F"

        print(f"{self.name}'s Grade: {grade}")

    # Parent method for polymorphism
    def get_student_type(self):
        print(f"{self.name} is a general student.")

    # Method Overloading using *args
    def add_marks(self, *marks):
        total = sum(marks)
        print(f"Total marks: {total}")

# Undergraduate Student

class UndergraduateStudent(Student):

    def __init__(self,name,student_id,email,age,department,marks,semester):
        super().__init__(name,student_id,email,age,department,marks)
        self.semester = semester
    # Method Overriding
    def get_student_type(self):
        print(f"{self.name} is an Undergraduate Student.")

    def show_program(self):
        print(
            f"{self.name} is studying "
            f"{self.department}, "
            f"Semester: {self.semester}"
        )

# Graduate Student

class GraduateStudent(Student):

    def __init__(self,name,student_id,email,age,department,marks,research_topic):
        super().__init__(name,student_id,email,age,department,marks)
        self.research_topic = research_topic

    # Method Overriding
    def get_student_type(self):
        print(f"{self.name} is a Graduate Student.")

    def show_research(self):
        print(
            f"{self.name}'s Research Topic: "
            f"{self.research_topic}"
        )

# Creating Objects
student1 = Student("Affan","1101","affan@gmail.com",20,"Mathematics",79)

student2 = UndergraduateStudent("Arifa","1102","arifa@gmail.com",21,"Mathematics",87,"2nd")

student3 = GraduateStudent("Himel","1103","himel@gmail.com",25,"Computer Science",79,"Data Science")


# Display Information
# =========================================================

student1.display_info()

student2.display_info()
student2.show_program()

student3.display_info()
student3.show_research()

# Calculate Results
student1.calculate_result()
student2.calculate_result()
student3.calculate_result()


# Polymorphism
# Same method, different behavior
# =========================================================

print("\n--- Polymorphism ---")

students = [student1, student2, student3]

for student in students:
    student.get_student_type()


# =========================================================
# Method Overloading using *args
# =========================================================

print("\n--- Method Overloading ---")

student1.add_marks(20)
student1.add_marks(20, 30)
student1.add_marks(20, 30, 40)


# =========================================================
# Encapsulation
# =========================================================

print("\n--- Encapsulation ---")

print("Student Email:", student1.get_email())
print("Student Marks:", student1.get_marks())


# Updating marks
student1.update_marks(85)

print("Updated Marks:", student1.get_marks())  