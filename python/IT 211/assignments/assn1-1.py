value1 = eval(input("Enter a number: "))
value2 = eval(input("Enter another number: "))
value3 = eval(input("Enter one more number: "))

list = [value1,value2,value3]
average = str(sum(list) / len(list))
print("The average of the three numbers is " + average +".")
