#!D:\Users\wucl\AppData\Local\Programs\Python\Python38-32
# -*- encoding: utf-8 -*-
'''
@文件    :20200415-moveFile.py
@说明    :将“D:\\Users\\wucl\\Desktop\\Downloads”里面的pdf文件移动到“D:\\Users\\wucl\\Desktop\\Downloads\\起点财经”里特定日期文件夹
@时间    :2020/04/16 10:39:11
@作者    :Max
@版本    :1.0
'''

import os, datetime, shutil

downLoadDir = 'D:\\Users\\wucl\\Desktop\\Downloads'
qiDianDir = 'D:\\Users\\wucl\\Desktop\\Downloads\\起点财经'

dt = datetime.datetime.now()

currentDay = dt.strftime('%Y') + dt.strftime('%m') + dt.strftime('%d')

subDir = qiDianDir + '\\' + currentDay

if not os.path.exists(subDir):
    os.makedirs(subDir)

for file in os.listdir(downLoadDir):
    fileName = os.path.splitext(file)[0]
    fileType = os.path.splitext(file)[1]
    fullPath = os.path.join(downLoadDir, file)
    if fileType == '.pdf':
        shutil.move(fullPath, subDir)

input("press any key to exit;")
