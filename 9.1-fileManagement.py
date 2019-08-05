import shutil, os
os.chdir('D:\\Users\\wucl\\iCloudDrive\\3GitHub\\python_learn\\test\\file')
workDir = os.getcwd()
testFile = 'test.txt'
fileName = os.path.join(workDir, testFile)
targetDir = os.path.join(workDir, 'fileTest')
shutil.copy(fileName, targetDir)
