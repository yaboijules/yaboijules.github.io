while True:
    try:
        check = eval(input("What is the value of the check? "))
    except:
        print('That is not a valid value')
        continue
    else:
        break
print('The total is $' + str(check) + '.')
while True:
    tip = input("Do you want to leave a good or bad tip? ")
    tip.lower()
    tip.strip()
    if tip == 'good' or tip =='bad':
        break
    else:
        print('Please enter if the tip was good or bad')
if tip == 'good':
    tipValue = check * .22
if tip == 'bad':
    tipValue = check * .15

print('You should tip $' + str(tipValue) + '.')
print('Your total will be $' + str(tipValue+check) + '.')
    

