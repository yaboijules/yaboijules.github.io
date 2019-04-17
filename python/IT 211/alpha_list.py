animals = []
while True:
    new = input('Name an animal. Enter d when done: ')
    if new.lower() == 'd':
        break
    else:
        animals.append(new)

# alpha_list = ['ant','bat','cow','dog']
for i in animals:
    print(i[0]+' is for '+i)

input()
