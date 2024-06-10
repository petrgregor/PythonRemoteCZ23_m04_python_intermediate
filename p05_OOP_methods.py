class Person:
    def __init__(self, name="Anonymous", age=0, **kwargs):
        self.name = name
        self.age = age
        self.other = kwargs

    def __str__(self):
        return f"{self.name} has age {self.age} years"


class Student(Person):
    variable = 2
    number_of_students = 0
    id_of_this_student = 0

    def __init__(self, name, age, scholarship):
        if self.is_name_correct(name):
            Person.__init__(self, name, age)
            self.scholarship = scholarship
            Student.number_of_students += 1
            self.id_of_this_student = Student.number_of_students
        else:
            raise TypeError

    def __str__(self):
        return f"{self.name} has age {self.age} years and scholarship {self.show_finance()}"

    def show_finance(self):
        return self.scholarship

    @classmethod
    def create_from_string(cls, sentence):
        name, age, scholarship = sentence.split()
        age = int(age)
        scholarship = float(scholarship)
        if cls.is_name_correct(name):
            return cls(name, age, scholarship)
        raise TypeError

    @staticmethod
    def is_name_correct(name):
        print("Static method 'is_name_correct' from class Student")
        if name[0].isupper() and len(name) >= 3:
            return True
        return False


def is_name_correct(name):
    print("Function 'is_name_correct'")
    if name[0].isupper() and len(name) >= 3:
        return True
    return False


student1 = Student("Martin", 20, 1500)
print(student1)
print(student1.show_finance())
print(student1.is_name_correct("Martin"))
print(Student.is_name_correct("Martin"))
print(is_name_correct("Martin"))

student2 = Student.create_from_string("Radek 21 2000")
print(student2)

student3 = Student.create_from_string("Max 21 600")
print(student3)

# static variable in class
print(student1.variable)
print(Student.variable)

student1.variable = 1
print(student1.variable)
print(Student.variable)

Student.variable = 10
print(student1.variable)
print(Student.variable)

print(Student.number_of_students)
student4 = Student('Roman', 25, 0)
print(f"Student.number_of_students: {Student.number_of_students}")
print(f"student4.number_of_students: {student4.number_of_students}")

print(f"student1.id_of_this_student: {student1.id_of_this_student}")
print(f"student2.id_of_this_student: {student2.id_of_this_student}")
print(f"student3.id_of_this_student: {student3.id_of_this_student}")
print(f"student4.id_of_this_student: {student4.id_of_this_student}")
