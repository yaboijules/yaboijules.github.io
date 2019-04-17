credits = eval(input("How many credits will you be taking next quarter? "))
if credits > 19:
    tuition = 12803 + (credits-18)*615
elif credits <= 18 and credits >= 12:
    tuition = 12803
elif credits < 12 and credits > 0:
    tuition = credits * 615

if credits == 0:
    print('you dont even go to school here')
else:
    print('Your tuition is $' + str(tuition) + '.')
