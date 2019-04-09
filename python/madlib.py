def getword(type):
	while True:
		word = input('Enter a '+type+'! ')
		if word:
			return word
		else:
			print('Please enter a word! ')

noun = []
adjective = []
adverb = []
while True:
	if len(adverb) == 1:
		break
	for i in range(7):
		noun.append([getword('noun')])
		if noun[i][0][:1] in ['a','e','i','o','u']:
			noun[i].append('an ') 
		else:
			noun[i].append('a ')
	for j in range(3):
		adjective.append([getword('adjective')])
		if adjective[j][0][:1] in ['a','e','i','o','u']:
			adjective[j].append('an ')
		else:
			adjective[j].append('a ')
	for k in range(1):
		adverb.append([getword('adverb')])
		if adverb[k][0][:1] in ['a','e','i','o','u']:
			adverb[k].append('an ')
		else:
			adverb[k].append('a ')
			
print(noun, adjective, adverb)

print()
print("Driving a car can be fun if you follow this "+adverb[0][0]+" advice:")
print("When approaching "+noun[0][1]+noun[0][0]+" on the right, always blow your "+noun[1][0]+".")
print("Before making "+adjective[0][1]+adjective[0][0]+" turn, always stick your "+noun[2][0]+" out of the window.")
print("Every 2000 miles, have your "+noun[3][0]+" inspected and your "+noun[4][0]+" checked.")
print("When approaching a school, watch out for "+adjective[1][0]+" "+noun[5][0]+".")
print("Above all, drive "+adjective[2][0]+". The "+noun[6][0]+" you save may be your own!")

input()
