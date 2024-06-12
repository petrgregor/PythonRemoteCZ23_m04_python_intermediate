"""
Task 2

Write a function that converts CSV to JSON.
"""
import csv
import json


def csv2json(_csv_file):
    reader = csv.reader(_csv_file)
    header = next(reader)
    #print(f"header = {header}")
    _json_result = []
    for row in reader:
        #print(row)
        us_peak_chart_post = row[2].strip()
        try:
            us_peak_chart_post = int(us_peak_chart_post)
        except ValueError as e:
            pass
            # print(f"ValueError: {e}")
        _json_result.append({header[0].strip(): row[0].strip(),
                             header[1].strip(): int(row[1].strip()),
                             header[2].strip(): us_peak_chart_post})
    return _json_result


def json_dump(json_data=None, indent=2, level=0):
    #print(f"json_data: {json_data}")
    result = ""
    if isinstance(json_data, list):
        result += "["
        level += 1
        for item in json_data:
            if indent:
                result += f"\n{' ' * level * indent}"
            result += json_dump(item, indent=indent, level=level)
        level -= 1
        result = result[:-1]
        if indent:
            result += f"\n{' ' * level * indent}"
        result += "]"
    elif isinstance(json_data, dict):
        #print(json_data)
        result += "{"
        level += 1
        for key in json_data:
            if indent:
                result += f"\n{' ' * level * indent}"
            result += f'"{key}": "{json_data[key]}",'
        level -= 1
        result = result[:-1]
        if indent:
            result += f"\n{' ' * level * indent}"
        result += "},"
    #print(result)
    return result


try:
    with open("p17_data.csv") as csv_file:
        json_result = csv2json(csv_file)
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

try:
    with open("p17_data.json", 'w') as json_file:
        result = json_dump(json_result, indent=3)
        #print(result)
        json_file.write(result)
        print("Export to json file done.")
except NameError as e:
    print(f"NameError: {e}")


# TODO: (bonus) definujte funkci json2csv
