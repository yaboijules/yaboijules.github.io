from random import randint
from time import sleep
from sys import exit

def checkint(x):
	try:
		int(x)
		return True
	except ValueError:
		print('Please enter a whole number!')
		return False

print('Welcome to the number guessing game! I will')
print('think of a number and you will try and guess')
print('what it is. I will tell you if the number is')
print('higher or lower than what you guessed.')
input('Press enter if you understand.')
print()

while True:
	print('Great! Let me think of a number.')
	for j in range(2):
			for i in range(5):
				print("Thinking" + "." * i + "      ", end='\r')
				sleep(.333)

	goal = randint(1,100)
	print('Okay I have a number!')
	guesscount = 0
	while True:
		while True:
			guess = input("What's your guess? ")
			if checkint(guess):
				guess = int(guess)
				break
		if guess > goal:
			print('Nope! Too high.')
			guesscount += 1
		if guess < goal:
			print('Nope! Too low.')
			guesscount += 1
		if guess == goal:
			print("That's my number! It took you "+ str(guesscount) + " guesses.")
			again = input('would you like to play again? enter y for yes and anything else to quit.')
			if again == 'y':
				print()
				break
			else:
				exit()
