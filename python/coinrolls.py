import math

def checknumber(x):
	try:
		float(x)
		return True
	except:
		print('Please enter a number')
		return False


while True:
	pgrams = input('How many grams of pennies do you have? ' )
	if checknumber(pgrams):
		pgrams = float(pgrams)
		break

while True:
	ngrams = input('How many grams of nickels do you have? ' )
	if checknumber(ngrams):
		ngrams = float(ngrams)
		break

while True:
	dgrams = input('How many grams of dimes do you have? ' )
	if checknumber(dgrams):
		dgrams = float(dgrams)
		break

while True:
	qgrams = input('How many grams of quarters do you have? ' )
	if checknumber(qgrams):
		qgrams = float(qgrams)
		break

print('')

pnum = pgrams/2.5
prolls = str(math.ceil(pnum/50))
print('You need '+prolls+' penny coin wrappers.')

nnum = ngrams/5
nrolls = str(math.ceil(nnum/40))
print('You need '+nrolls+' nickel coin wrappers.')

dnum = dgrams/2.268
drolls = str(math.ceil(dnum/50))
print('You need '+drolls+' dime coin wrappers.')

qnum = qgrams/5.67
qrolls = str(math.ceil(qnum/40))
print('You need '+qrolls+' quarter coin wrappers.')

input()