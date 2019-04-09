while True:
	value = input("Enter a number: ")

	if value == 'q':
		print("Exiting program (break statement")
		break

	if not value.isdigit():
		print("Enter digits only(cont statement)")
		continue

	value = int(value)
	print('Cube of', value, "is", value**3)