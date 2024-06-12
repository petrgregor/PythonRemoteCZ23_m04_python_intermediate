"""
Serialization
Task 1

You have a text file with the content:

{
   "right_side":[
      3,
      5,
      3,
      6,
      4,
      2,
      3,
      6,
      8,
      4,
      3,
      2
   ],
   "left_side":[
      1.2,
      4.3,
      5.4,
      6.9,
      9.9,
      7.2
   ]
}

Write a program that prints the average of the numbers in the "right_side" field,
the average of the "left_side" field,
and the average of both fields.
"""
from json import load


def only_numbers(_data):
    numbers = []
    for item in _data:
        if isinstance(item, int) or isinstance(item, float):
            numbers.append(item)
    return numbers


def average(_data):
    #print(f"Original data: {_data}")
    _only_numbers = only_numbers(_data)
    #print(f"Only numbers:  {_only_numbers}")
    return sum(_only_numbers) / len(_only_numbers)


with open("p16_data.json", "r") as f:
    data = load(f)
    #print(data)
    """avg_right = average(data['right_side'])
    print(f"Average right side: {avg_right}")
    avg_left = average(data['left_side'])
    print(f"Average left side: {avg_left}")
    data_all = data['right_side'] + data['left_side']
    avg_all = average(data_all)
    print(f"Average all: {avg_all}")"""

    print(f"Average right side: {average(data['right_side'])}")
    print(f"Average left side: {average(data['left_side'])}")
    print(f"Average all: {average(data['right_side'] + data['left_side'])}")
