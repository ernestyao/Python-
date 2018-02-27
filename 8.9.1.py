#! python 3
'''
Created on Feb 25, 2018
Solution for Ch 8;
@author: ern
'''

# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
# py.exe mcb.pyw delete <keyword> - Deletes keywords in the list.
# py.exe mcb.pyw delete - Deletes all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	try:
		del mcbShelf[sys.argv[2]]
	except KeyError:
		print('No such keyword found.')
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	elif sys.argv[1].lower() == 'delete':
		for key in mcbShelf:
			del mcbShelf[key]

mcbShelf.close()