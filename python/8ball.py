from random import randint
from time import sleep

playing = True

while playing:
	response = input("What would you like to ask the magic 8 ball? ")
	if response == 'q':
		playing = false
		break

	ans = randint(0,19)

	
	for j in range(0,randint(1,6)):
		for i in range(0,5):
			print("Thinking" + "." * i + "      ", end='\r')
			sleep(.333)
	

	if ans == 0:
		print('It is certain.')
	elif ans == 1:
		print('It is decidedly so.')
	elif ans == 2:
		print('Without a doubt.')
	elif ans == 3:
		print('Yes - definitely.')
	elif ans == 4:
		print('You may rely on it.')
	elif ans == 5:
		print('As I see it, yes.')
	elif ans == 6:
		print('Most likely.')
	elif ans == 7:
		print('Reply hazy, try again.')
	elif ans == 8:
		print('Ask again later.')
	elif ans == 9:
		print('Better not tell you now.')
	elif ans == 10:
		print('Cannot predict now.')
	elif ans == 11:
		print('Concentrate and ask again.')
	elif ans == 12:
		print("Don't count on it.")
	elif ans == 13:
		print('My reply is no.')
	elif ans == 14:
		print('My sources say no.')
	elif ans == 15:
		print('Outlook not so good.')
	elif ans == 16:
		print('Very doubtful.')
	elif ans == 17:
		print('Outlook good.')
	elif ans == 18:
		print('Yes.')
	elif ans == 19:
		print('Signs point to yes.')

	print('')


