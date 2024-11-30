import self
class Student():
    def __init__(self,name,surname,age,average_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self,new_grade):
            self.average_grade = new_grade

    def __str__(self):
        return f"Ім'я: {self.name}, Прізвище: {self.surname}, Вік: {self.age}, Середній бал: {self.average_grade}"


student = Student("Михайло ","Корчак", 28,85.5)
print("Інформарція про студента ")
print(student)
student.update_average_grade(90)
print("\nОновлення інформація про студента ")
print(student)