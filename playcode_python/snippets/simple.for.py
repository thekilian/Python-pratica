'''
# 5. more pythonic form with position
surnames = ['Rivest', 'Shamir', 'Adleman']
for position, surname in enumerate(surnames):
    print(position, surname)
'''

'''
# 4. more pythonic form
surnames = ['Rivest', 'Shamir', 'Adleman']
for surname in surnames:
    print(surname)
'''

'''
# 3. iterating over a sequence
surnames = ['Rivest', 'Shamir', 'Adleman']
for position in range(len(surnames)):
    print(position, surnames[position])
'''

'''
# 2. iterating over a range
for number in range(5):
    print(number)
'''

'''
# 1. the for loop
for number in [0, 1, 2, 3, 4]:
    print(number)
'''