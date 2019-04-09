number = list(range(99,0,-1))

for i in number:
	if i == 1:
		bottles = "bottle"
	else: 
		bottles = "bottles"
	print(i, bottles, "of beer on the wall,")
	print(i, bottles, "of beer,")
	print("take one down, pass it around,")
	print(i, bottles, "of beer on the wall.")
	print('')

input()