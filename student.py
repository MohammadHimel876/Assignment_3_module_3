class student:
    def __init__(self,name,student_id,email,marks,department):
        self.name=name
        self.student_id=student_id
        self.__email=email
        self.__marks=marks
        self.department=department


    def get_email(self):
        return self.__email

    def get_marks(self):
        return self.__marks
    # def update_email(self,email):


    def update_marks(self,marks):

        if 0<=marks<=100:
            self.__marks
        else :
            print("Invalid marks")


    def display_info(self):

        print(f"Name: {self.name}")
        print(f"Student_ID: {self.name}")
        print(f"E-mail: {self.__email}")
        print(f"Marks: {self.__marks}")
        print(f"Department: {self.department}")

    def calculate_result(self):
        print(f"i am a {self.__marks}")
        if self.__marks>=80:
            print("A+")
        elif self.__marks>=70:
            print("A")
        elif self.__marks>=60:
            print("A-")
        elif self.__marks>=50:
            print("B")
        elif self.__marks>=40:
            print("C")
        elif self.__marks>=33:
            print("D")
        else:
            print("F")


    def add_marks(self,*marks):
        return sum(marks)

# print(s1.name)
# s1.display_info()

class UndergraduateStudent(student):

    def __init__(self,name,student_id,email,age,semester,department):
        super().__init__(name,student_id,email,age,department)
        self.semester = semester
        
    def show_program(self):
        print(
        f"{self.name} is studying "
        f"{self.department}, "
        f"Semester {self.semester}")
    
    def get_student_type(self):
        print(f"i am a {self.name}")


class GraduateStudent(student):
    def __init__(self,name,student_id,email,marks,department,research_topic):
        super().__init__(name,student_id,email,marks,department)
        self.research_topic = research_topic

    def get_student_type(self):
        print(f"i am a {self.name}")




affan=student("himel","1101","hemel@gmail.com",79,"math")
arifa=UndergraduateStudent("himel","1101","hemel@gmail.com",87,"math","2nd")
himel=GraduateStudent("himel","1101","hemel@gmail.com",79,"math","Data_Science")
affan.display_info()
arifa.show_program()
affan.calculate_result()