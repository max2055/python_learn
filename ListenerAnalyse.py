import os
import re

workDir = 'D:\\Users\\wucl\\Desktop\\logs\\TNS\\lsnrlog-10.17.18.28-2019'
resultFile = 'D:\\Users\\wucl\\Desktop\\logs\\TNS\\lsnr-10.17.18.28-2019.txt'
ipRegex = re.compile(
    r'''(
    \(
    HOST\=
    (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
    \)\(
    PORT\=
    (\d{1,5})
    \)
    )''', re.VERBOSE)

ipFile = open(resultFile, 'w')

# 获取文件夹内的文件列表
for folderName, subfolders, filenames in os.walk(workDir):
    # print(folderName)
    # print(subfolders)
    # print(filenames)
    # 依次读取文件内容，根据正则表达式进行匹配
    for filename in filenames:
        lnsrFile = open(folderName + '\\' + filename)
        lnsrContent = lnsrFile.readlines()
        for line in lnsrContent:
            targetIP = ipRegex.findall(line)
            # print(line)
            if len(targetIP) >= 1:
                print(targetIP[0][0])
            # print(len(targetIP))
                ipFile.write(str(targetIP[0][0]))
                ipFile.write('\n')
ipFile.close()
