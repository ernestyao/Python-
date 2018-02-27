#! python 3
'''
Created on Feb 22, 2018
Solution for Ch 6
@author: ern
'''
def printTable(table):
	colWidth = [0]*len(table)
	for i in range(len(table)):
		for word in table[i]:
			if colWidth[i] < len(word):
				colWidth[i] = len(word)	
	result = [[0 for i in range(len(table))] for j in range(len(table[0]))]

	for i in range(len(table)):
		for j in range(len(table[0])):
			result[j][i] = table[i][j].rjust(colWidth[i])

	for i in range(len(result)):
		print('\t'.join(result[i]))


tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)