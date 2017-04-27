import json

numbers = [1, 2, 3, 4, 5, 6]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

file_path = 'D:/Desktop/OneDrive/GitHub/python_learn/file_test.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    for line in file_object:
        print(line.rstrip())

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
