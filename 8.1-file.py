# # 1. path
# import os
# print(os.path.join('c:\\', 'Windows', 'etc'))
# print(os.getcwd())
# # print(os.chdir('d:\\'))
# # print(os.getcwd())
# # os.makedirs('D:\\Users\\wucl\\Desktop\\Test\\t1')
# print(os.path.abspath('.'))
# print(os.path.isabs('.'))
# print(os.path.isabs(os.path.abspath('.')))
# print(
#     os.path.relpath('D:\\Users\\wucl\\Desktop\\Test\\t1'))
# print(os.path.dirname('D:\\Users\\wucl\\Desktop\\Test\\t1'))
# print(os.path.basename('D:\\Users\\wucl\\Desktop\\Test\\t1'))
# print(os.path.split('D:\\Users\\wucl\\Desktop\\Test\\t1'))

# # 2. operation
# helloFile = open(os.path.join(os.getcwd(), 'python_learn', 'hello.txt'), 'r')
# print(helloFile.readlines())
# helloFile.close()
# helloFile = open(os.path.join(os.getcwd(), 'python_learn', 'hello.txt'), 'a')
# helloFile.write('\nyou are welcome')
# helloFile.close()
# helloFile = open(os.path.join(os.getcwd(), 'python_learn', 'hello.txt'), 'r')
# print(helloFile.readlines())
# helloFile.close()

# 3. shelve
import shelve, os
os.getcwd()
os.chdir('D:\\Users\\wucl\\iCloudDrive\\3GitHub\\python_learn\\test\\shelve')
shelFile = shelve.open('mydata')
cats = ['soc', 'pooka']
shelFile['cats'] = cats
shelFile.close()
shelFile = shelve.open('mydata')
print(type(shelFile))
print(shelFile['cats'])
shelFile.close()
shelFile=shelve.open('mydata')
print(list(shelFile.keys()))
print(list(shelFile.values()))
shelFile.close()