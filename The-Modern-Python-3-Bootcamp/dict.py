#dictionary practice

cat = {'name' : 'blue', 'age' : 3.5, 'isCute' : True}

# another_dictionary = dict(key = 'value', key = 'value')

cat2 = dict(name='kitty', age=0.5)

cat['name'] # 'blue'
cat['age'] # 3.5

instructor = {
    'name': 'Colt',
    'owns_dog': True,
    'favorite_language': 'Python',
    'is_hilarious': False,
    44: 'my_favorite_number'
    }

# ADD SOMETHING TO DICTIONARY
instructor['cookie'] = 18
#'cookie' : 18
print(instructor)

for value in instructor.values():
    print(value)

# more common

for v in instructor.values():
    print(v)

for v in instructor.keys():
    print(v)

for key,value in instructor.items():
    print(f'Key is {key} and value is {value}')

'name' in instructor
#True
'phone' in instructor
#False

if 'name' in instructor:
    print(instructor['name'])

'Colt' in instructor.values()
#True
