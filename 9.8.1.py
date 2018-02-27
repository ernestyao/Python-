#! python 3
'''
Created on Feb 26, 2018
Solution for Ch 9
@author: ern
'''
import os
import shutil

fromPath = '/Users/ern/Downloads'
toPath = '/Users/ern/'
for folderName, subfolders, filenames in os.walk(fromPath):
	for file in filenames:
		if file.endswith('.pdf'):
			filePath = os.path.join(folderName, file)
			shutil.copy(filePath, toPath)
