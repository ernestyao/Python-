#! python 3
'''
Created on Feb 26, 2018
Solution for Ch 9
Modify the original problem to list the whole file list ordered by filesize desc
@author: ern
'''
import os
import shutil

fileList = {}

targetPath=os.getcwd()
for folder, subfolders, filenames in os.walk(targetPath):
	for file in filenames:
		filePath = os.path.join(folder, file)
		fileList[filePath] = os.path.getsize(filePath)
fileListSort = sorted(fileList.items(), key = lambda x: x[1], reverse = True)
for fns in fileListSort:
	print(fns[0],str(fns[1]).rjust(10))
