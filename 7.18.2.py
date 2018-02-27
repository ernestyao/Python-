#! python 3
'''
Created on Feb 23, 2018
Solution for Ch 7
@author: ern
'''
import re

def strip(str, strToStrip=''):
	if strToStrip == '':
		strExp = re.compile(r'[^\s]')
	else:
		strExp = re.compile(r'[^' + strToStrip + ']')
	mo = strExp.findall(str)
	return (''.join(mo))

result = strip('woehohbojwro', 'owh')
print(result+str(len(result)))
result = strip(' sjdofjeif ')
print(result+str(len(result)))