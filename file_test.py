#f = open('file_test.txt', 'r+', encoding='utf-8')
# f.write('test')
# f.write('\ntest2')
# f.write('\ntest3')

# print(f.readline())
# print(f.tell())
#
# print(f.seek(1))
# print(f.readline())
# print(f.tell())
# f.seekable()
# print(f.tell())
# print(f.seek(1))
# f.truncate()
#
# f.close()


f = open('file_test.txt', 'r+', encoding='utf-8')

f.seek(2)

f.write("python测试test")
