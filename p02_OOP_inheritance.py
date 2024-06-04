class Person:
    def __init__(self, name="Anonymous", age=0, **kwargs):
        self.name = name
        self.age = age
        self.other = kwargs

    def __str__(self):
        #return f"{self.name} is {self.age} years old"
        return f"{self.name} has age {self.age} years"


class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        Person.__init__(self, age=age, name=name)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def __str__(self):
        #return f"{self.name} is {self.age} years old with finance {self.show_finance()}"
        return f"{super().__str__()} with finance {self.show_finance()}"

    def show_finance(self):
        return self.rate * self.num_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def __str__(self):
        return f"{super().__str__()} with finance {self.show_finance()}"

    def show_finance(self):
        return self.scholarship


class WorkingStudent(Employee, Student):
    def __init__(self, name, age, rate, num_of_hours, scholarship):
        Employee.__init__(self, name, age, rate, num_of_hours)
        Student.__init__(self, name, age, scholarship)

    def __str__(self):
        return f"{Person.__str__(self)} with finance {self.show_finance()}"

    def show_finance(self):
        return self.rate * self.num_of_hours + self.scholarship


os1 = Person("John", 54)
print(os1)
os2 = Employee("Jack", 36, 20, 1000)
print(os2)
os3 = Student("Agatha", 22, 1000)
print(os3)
os4 = WorkingStudent("Monica", 24, 9.5, 70, 550)
print(os4)
