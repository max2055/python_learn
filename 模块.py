import my_module
import time
import datetime
import shutil

my_module.sayhi('max')


import sys,os

print(dir())
print(__file__)

a = time.strftime('%Y %m-%d %H:%M:%S %A')
print(a)

b = time.strptime(a,'%Y %m-%d %H:%M:%S %A')
print(b)

c = time.mktime(b)
print(c)

d = datetime.datetime.now()
print(d)
print(d.year)

cwd = os.getcwd()
print(cwd)
os.chdir(cwd)
cwd = os.getcwd()
print(cwd)
shutil.copytree("test", "test1")