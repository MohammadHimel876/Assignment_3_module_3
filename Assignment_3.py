class Student:

    university = "ABC University"

    def __init__(self, name, student_id, email, marks):

        self.name = name
        self.student_id = student_id

        self.__email = email
        self.__marks = marks

    #     self.courses = []

    # def get_email(self):
    #     return self.__email

    # def update_email(self, new_email):

    #     if "@" in new_email:
    #         self.__email = new_email
    #         print("Email updated successfully.")
    #     else:
    #         print("Invalid email.")

    # def get_marks(self):
    #     return self.__marks

    # def update_marks(self, marks):

    #     if 0 <= marks <= 100:
    #         self.__marks = marks
    #         print("Marks updated.")
    #     else:
    #         print("Marks must be between 0 and 100.")

    # def enroll_course(self, course):

    #     self.courses.append(course)

    #     print(
    #         f"{self.name} enrolled in {course.name}"
    #     )

    # def show_courses(self):

    #     if not self.courses:
    #         print("No courses enrolled.")
    #         return

    #     print(f"\n{self.name}'s Courses:")

    #     for course in self.courses:
    #         print(
    #             f"- {course.code}: "
    #             f"{course.name}"
    #         )

    # def show_info(self):

    #     print("\n----- Student Information -----")

    #     print(f"University: {self.university}")
    #     print(f"Name: {self.name}")
    #     print(f"Student ID: {self.student_id}")
    #     print(f"Email: {self.__email}")
    #     print(f"Marks: {self.__marks}")

    # def calculate_grade(self):

    #     marks = self.__marks

    #     if marks >= 80:
    #         return "A+"
    #     elif marks >= 70:
    #         return "A"
    #     elif marks >= 60:
    #         return "B"
    #     elif marks >= 50:
    #         return "C"
    #     else:
    #         return "F"

    # def add_marks(self, *marks):

    #     total = sum(marks)

    #     print(f"Total marks: {total}")

    #     return total


class UndergraduateStudent(Student):

    def __init__(self,name,student_id,email,marks,semester,department):
        super().__init__(name,student_id,email,marks)
        self.semester = semester
        self.department = department
    def show_program(self):
        print(
        f"{self.name} is studying "
        f"{self.department}, "
        f"Semester {self.semester}")

# s1=Student("himel","1001","hemel@",78)
s1=UndergraduateStudent("himel","1001","hemel@",78,"adahfd","math")
s1.show_program()
