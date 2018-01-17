import getpass

print('Hello,%s'%'world')
print('%2d-%02d'%(3,1))
print('%.2f'%3.1415926)
print('growth rate:%d%%' %7)
s1=72
s2=85
r=(s2-s1)/s1*100
if (r>0):
    print('increase by %.1f%%'%r)
elif (r<0):
    print('decrease by %.1f%%'%(-r))
else: 
    print ('no change')
    
names=['zhang','wang','li','chen','zhu']
print(sorted(names))
print(sorted(names,reverse=True))
print(len(names))
#names=['zhang','wang','li','chen','zhu']
for name in names:
    print(name)
print('hello everyone')
for value in range(1,5):
    print(value)
numbers1=list(range(1,8))
print(numbers1)
numbers2=list(range(2,22,2))
print(numbers2)
squares=[value**2 for value in range(1,10,3)]
print(squares)

for county in menu[prov]:
    print(county)
    for zone in menu[prov][county]:
        print(zone)
        for company in menu[prov][county][zone]:
            print(company)