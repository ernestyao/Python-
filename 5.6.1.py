'''
Created on Feb 21, 2018
Solution for Ch 5
@author: ern
'''
# Solution1
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total += v
    print ('Total number of items: ' + str(total))

displayInventory(stuff)