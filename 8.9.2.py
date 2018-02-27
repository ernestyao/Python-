#! python 3
'''
Created on Feb 25, 2018
Solution for Ch 8
@author: ern
'''
import os
import re

wordToRepl = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

fileDir = os.getcwd()
filePath = os.path.join(fileDir, '8.9.2.txt')

file = open(filePath, 'r')
fileContent = file.read()
#print(fileContent)
wordRegex = re.compile(r'\w+')
wordList = wordRegex.findall(fileContent)
#print(wordList)
for word in wordList:
	if word in wordToRepl:
		print('Enter a ' + word.lower() + ':')
		wordNew = input()
		fileContent = fileContent.replace(word, wordNew)
print(fileContent)
resultPath = os.path.join(fileDir, '8.9.2_result.txt')
result = open(resultPath, 'w')
result.write(fileContent)
file.close()
result.close()
