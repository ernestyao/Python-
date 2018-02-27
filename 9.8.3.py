#! python 3
'''
Created on Feb 27, 2018
Solution for Ch 9
@author: ern
'''
import os
import shutil
import re

prefix = 'spam' #可以按照需要改成input()输入或程序的命令行参数
filePath = os.getcwd()
fileList = {}
fnRegex = re.compile(prefix + r'(\d+)')
for file in os.listdir(filePath):
	mo = fnRegex.search(file)
	if mo != None:
		fileList[file] = mo.group(1)
fileSort = sorted(fileList.items(), key = lambda x:int(x[1]))
print(fileSort)

i = 0
for fn in fileSort:
	if int(fn[1]) > i + 1:
		i += 1
		newFile = prefix + str(i).zfill(len(fn[1])) + os.path.splitext(fn[0])[1] #根据原字符串长度补齐前面的0
		fromFile = os.path.join(filePath, fn[0])
		toFile = os.path.join(filePath, newFile)
		print('%s move to %s' % (fromFile, toFile))
		shutil.move(fromFile, toFile)
	else:
		i += 1