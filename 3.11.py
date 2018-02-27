'''
Created on Feb 21, 2018
Solution for Ch 3
@author: ern
'''
# This is Collatz sequence demo.
def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
    else:
        number = number * 3 + 1
        print(number)
    return number
        
print('Input a start number')
try:
    n = int(input())
    while (n != 1):
        n = collatz(n)
except ValueError:
    print("Invalid input. Please input an integer.")
        