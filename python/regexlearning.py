import re

while True:
	message = input('enter some text. itll look for a phone number ')
	phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	found = phoneRegex.search(message)
	print('Phone number found: '+found.group())