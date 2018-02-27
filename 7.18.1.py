#! python 3
'''
Created on Feb 22, 2018
Solution for Ch 7
@author: ern
'''
import re

def isStrongPwd(pwd):
	AlphaRex = re.compile(r'([A-Z]+[a-z]+)|([a-z]+[A-Z]+)')
	NumRex = re.compile(r'\d+')
	if len(pwd) < 8:
		return False
	elif AlphaRex.search(pwd) == None or NumRex.search(pwd) == None:
		return False
	else:
		return True


testPwd='123456^&((\n&$##aB'
print(testPwd + ' is' + [' not',''][isStrongPwd(testPwd)] +' a strong password.')
