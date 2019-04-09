def thefunction(a,b,c):
	if (pow(a,2) + pow(b,2) == pow(c,2)):
		print('It is a pythagorean triple')
	else:
		print('It is not a pythagorean triple')

def checkdigit(x):
	try:
		int(x)
		return True
	except ValueError:
		print('That is not a valid number.')
		return False

go = True
while go:
	while True:
		hypotenuse = input('How long is the longest side of the triangle? ')
		if checkdigit(hypotenuse):
			hypotenuse = int(hypotenuse)
			break

	while True:
		side1 = input('How long is one of the other sides? ')
		if checkdigit(side1):
			side1 = int(side1)
			break

	while True:
		side2 = input('How long is the last side? ')
		if checkdigit(side2):
			side2 = int(side2)
			break

	thefunction(side1,side2,hypotenuse)

	quit = input('press enter to go again, type q to quit ')
	if quit == 'q':
		go = False
