'''
Created on Feb 21, 2018
Solution for Ch 4
@author: ern
'''
# Solution1
def spand(listIn):
    strOut = ''
    if len(listIn) == 1:
        strOut += listIn[0]
    elif len(listIn) == 0:
        strOut = ''
    else:
        for i in listIn[:-1]:
            strOut = strOut + i + ', '
        strOut = strOut + 'and ' + listIn[-1]
    return strOut

spam = ['apples', 'bananas', 'tofu', 'cats']
print(spand(spam))
