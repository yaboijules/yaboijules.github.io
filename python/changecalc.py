import math

while True:	
	total = input('What is the total? ')
	try:
		float(total)
		break
	except ValueError:
		print('Please enter a number.')

while True:
	tender = input('How much money was tendered? ')
	try:
		float(tender)
		break
	except ValueError:
		print('Please enter a number.')

change = float(tender) - float(total)

twentybill = math.floor(change/20)
remaining = change%20
tenbill = math.floor(remaining/10)
remaining = remaining%10
fivebill = math.floor(remaining/5)
remaining = remaining%5
onebill = math.floor(remaining/1)
remaining = remaining%1
quarters = math.floor(remaining/.25)
remaining = change%.25
dimes = math.floor(remaining/.1)
remaining = remaining%.1
nickles = math.floor(remaining/.05)
remaining = remaining%.05
pennies = math.floor(remaining/.01)

print("Their change is:")
if twentybill:
	print(str(twentybill)+" $20 bills")
if tenbill:
	print(str(tenbill)+" $10 bills")
if fivebill:
	print(str(fivebill)+" $5 bills")
if onebill:
	print(str(onebill)+" $1 bills")
if quarters:
	print(str(quarters)+" quarters")
if dimes:
	print(str(dimes)+" dimes")
if nickles:
	print(str(nickles)+" nickles")
if pennies:
	print(str(pennies)+" pennies")

input()