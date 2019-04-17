import random

noun = input('Enter a noun: ')
adjective = input('Enter an adjective: ')
noun_list = ['house','car','tunnel','castle','field']
print('The ' + adjective + ' ' + noun + ' is in the ' + random.choice(noun_list) + '.')
