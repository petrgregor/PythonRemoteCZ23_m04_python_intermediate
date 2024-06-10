import csv


class Employee:

    def __init__(self, name_surname, salary, age):
        self.name, self.surname = name_surname.split()
        self.salary = salary
        self.age = age

    def __repr__(self):
        return (f"Employee("
                f"name={self.name}, "
                f"surname={self.surname}, "
                f"salary={self.salary}, "
                f"age={self.age}"
                f")")

    @classmethod
    def create_from_list(cls, employee_list):
        name_surname = employee_list[0]
        salary = int(employee_list[1])
        age = int(employee_list[2])
        return cls(name_surname, salary, age)

    def to_csv(self):
        return f"{self.name} {self.surname}, {self.salary}, {self.age}"

    def to_csv_list(self):
        return [f"{self.name} {self.surname}", f" {self.salary}", f" {self.age}"]


with open('employees.csv') as f:
    reader = csv.reader(f)
    # print(reader.line_num)
    # reader_list = list(reader)
    # print(reader_list[2])
    # print(reader_list)
    next(reader)  # skip first line
    employees = []
    for row in reader:
        print(row)
        employees.append(Employee.create_from_list(row))

    print(employees)
    for employee in employees:
        print(employee)

with open('employees_output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    #writer.writerow("employee, salary, age".split(", "))  # header
    writer.writerow(["employee", " salary", " age"])  # header
    for employee in employees:
        #writer.writerow(employee.to_csv().split(", "))
        writer.writerow(employee.to_csv_list())
        #print(employee.to_csv())
        #print(employee.to_csv().split(", "))
