class Student:

    class_year = 2016
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1


stud1 = Student('Mr.Bean',45)
stud2 = Student('Pao', 21)
stud3 = Student('Ang',20)
stud4 = Student('CocoM',67)

print(stud2.name)
print(stud1.age)
print(Student.class_year)

print(Student.num_students)
print("------------------------------")
print(f"My class of {Student.class_year} has {Student.num_students} Students")
print(stud1.name)
print(stud2.name)
print(stud3.name)
print(stud4.name)
print("------------------------------")
