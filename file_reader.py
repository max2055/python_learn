import json
import chardet

numbers = [1, 2, 3, 4, 5, 6]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

file_path = 'D:/Desktop/OneDrive/3GitHub/python_learn/file_test.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    for line in file_object:
        print(line.rstrip())

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

f = open("D:/Desktop/OneDrive/3GitHub/python_learn/list.py", "r", encoding="utf-8")
data = f.read()
print(data)
f.close()

# result = chardet.detect(f)
# print(result)
#

f = open('file_test.txt', 'w')
f.write('\ntest')
f.write('\ntest2')

f.readline()

f.close()
f.readable()

