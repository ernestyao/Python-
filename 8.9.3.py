#! python 3
'''
Created on Feb 26, 2018
Solution for Ch 8
@author: ern
'''
import os
import re

br = 0
print('Please input your regular expression:')
inputPattern = input()
try:
	inputRegex = re.compile(inputPattern)
	br = 1
except:
	print('Wrong input.')
if br != 0:	
	fileDir = os.getcwd()
	for fn in (fns for fns in os.listdir(fileDir) if fns.endswith('.txt')):
		#print(fn)
		fileName = os.path.join(fileDir, fn)
		file = open(fn, 'r')
		fileLines = file.readlines()
		for line in fileLines:
			result = inputRegex.match(line)
			if result != None:
				print(line)
		file.close()

