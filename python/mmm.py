import math

def checkint(x):
	try:
		int(x)
		return True
	except ValueError:
		print('Please enter a whole number!')
		return False

def findmedian(x):
	#------ makes new list in numerical order -------
	#------ also could have just used the .sort() list method
	medianlist = []
	holder = x[:]
	for i in range(len(holder)):
		medianlist.append(min(holder))
		holder.remove(medianlist[-1])
	if len(medianlist)%2 == 1:
		medianindex = math.floor(len(medianlist)/2)
		return [medianlist[medianindex]]
	elif len(medianlist)%2 == 0:
		medianindex1 = int((len(medianlist)/2)-1)
		medianindex2 = int(len(medianlist)/2)
		return [medianlist[medianindex1],medianlist[medianindex2]]

def findmode(x):
	x.append(min(x)-1)
	mode = x[-1]
	for i in range(min(x)+1,max(x)+1):
		if x.count(i) > x.count(mode):
			mode = i
	x.remove(min(x))
	if mode in x:
		return "The mode is "+ str(mode) +"."
	else:
		return "There is no mode."


# ---------- start program --------------------------
print("You will enter a series of numbers and this")
print("program will find the mean, median, and mode.")

numgroup = []
while True:
	number = input("Add a number, enter d when done: ")
	if number == 'd':
		break
	if checkint(number):
		numgroup.append(int(number))


while True:
	decplaces = input("How many decimal places do you want up to? ")
	if checkint(decplaces):
		decplaces = int(decplaces)
		break
#-------- mean -----------------------------------------
mean = round((sum(numgroup)/len(numgroup)),decplaces)
if mean%1 == 0:
	mean = int(mean)
print('The mean of these numbers is '+str(mean)+'.')
#----------- median -----------------------------------
median = findmedian(numgroup)
if len(median) > 1:
	print('The medians of these numbers are '+ str(median[0]) +' and '+ str(median[1]) +'.')
else:
	print('The median of these numbers is '+ str(median[0]) +'.')
#--------- mode -----------------------------------------
print(findmode(numgroup))






input('Press enter to exit.')
