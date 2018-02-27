'''
Created on Feb 21, 2018
Solution for Ch 4
@author: ern
'''
# Solution2
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

col = []
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print('')