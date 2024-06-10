import json

# writing to json
students = [
    {
        'name': "Adam",
        'surname': "Smith",
        'number of points': {
            'test a': 20,
            'test b': 25,
            'total': 45
        }
    },
    {
        'name': "John",
        'surname': "Shadow",
        'telephone': '+42077788899',
        'number of points': {
            'test a': 20,
            'test b': 25,
            'total': 45
        }
    }
]

with open('students.json', 'w') as f:
    json.dump(students, f, indent=3)

# reading from json file
with open('students.json', 'r') as f:
    students2 = json.load(f)

for student in students2:
    print(student)
